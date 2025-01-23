from upload_files.file_uploader import FileUploader
from db import db
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException


def create_file(request):
    with db.atomic():
        return execute(request)


def execute(request):
    file = (
        FileUploader.select().where(FileUploader.file_name == request.file_name).first()
    )
    if not file:
        file = FileUploader()
    update_params = get_create_params(request)
    for k, v in update_params.items():
        setattr(file, k, v)

    if not file.save():
        raise HTTPException(status_code=400, detail="could'nt save vessel information")

    return {"id": jsonable_encoder(file.id)}


def get_create_params(request):
    return request.dict(
        exclude_none=True,
    )
