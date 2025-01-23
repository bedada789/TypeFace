from upload_files.file_uploader import FileUploader
from operator import attrgetter
from fastapi.encoders import jsonable_encoder
from math import ceil
import json

def list_files(filters={}, page=1, page_limit=10, pagination_data_required=False):
    query = get_query()
    if isinstance(filters,str):
        filters = json.loads(filters)

    for key, value in filters.items():
        if getattr(FileUploader, key):
            query = query.where(attrgetter(key)(FileUploader) == value)
    pagination_data = {}
    if pagination_data_required:
        pagination_data = get_pagination_data(query, page, page_limit)
    if page_limit:
        query = query.paginate(page, page_limit)

    data = jsonable_encoder(list(query.dicts()))

    return {"list": data} | pagination_data


def get_query():
    query = FileUploader.select()
    return query


def get_pagination_data(query, page: int, page_limit: int) -> dict:
    total_count = query.count()
    return {
        "page": page,
        "total": ceil(total_count / page_limit),
        "total_count": total_count,
        "page_limit": page_limit,
    }
