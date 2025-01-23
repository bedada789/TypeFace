from fastapi import FastAPI,APIRouter
from fastapi.middleware.cors import CORSMiddleware
from upload_files.list_files import list_files
from upload_files.file_uploader import FileUploader
from db import db
from upload_files.api_router import api_router
from fastapi.staticfiles import StaticFiles

doc = {
    "debug": True,
    "docs_url":  "/docs",
    "openapi_url":  "/openapi.json",
    "swagger_ui_parameters": {"docExpansion": None},
}

app = FastAPI(**doc)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/files", StaticFiles(directory="uploaded_files"), name="files")

@app.get("/")
def read_root():
    return {"Application Started!!"}

app.include_router(prefix = "/api", router=api_router, tags=['Api'])

@app.on_event("startup")
def startup():

    if db.is_closed():
        db.connect()
        db.create_tables([FileUploader])
        print("created_tables")


