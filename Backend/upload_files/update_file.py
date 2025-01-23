from upload_files.file_uploader import FileUploader
from db import db
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException


def update_file(request):
    with db.atomic():
        return execute(request)


def execute(request):
    file = (
        FileUploader.select().where(FileUploader.id == request.id).first()
    )
    if not file:
        raise HTTPException(status_code=400,detail="File Not Foound")
    update_params = get_create_params(request)
    for k, v in update_params.items():
        setattr(file, k, v)

    if not file.save():
        raise HTTPException(status_code=400, detail="could'nt save File")

    return {"id": jsonable_encoder(file.id)}


def get_create_params(request):
    return request.dict(
        exclude_none=True,
    )
