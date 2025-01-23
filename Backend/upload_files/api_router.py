from fastapi import  APIRouter,  File, UploadFile
from fastapi.responses import JSONResponse
from upload_files.list_files import list_files
from upload_files.create_file import create_file
from upload_files.update_file import update_file
from fastapi import HTTPException
from pydantic import BaseModel
from pathlib import Path

api_router = APIRouter()

UPLOAD_DIR = Path("uploaded_files")
UPLOAD_DIR.mkdir(exist_ok=True)

class FileUploader(BaseModel):
    file_name: str
    file_path: str

class UpdateFile(BaseModel):
    id: int
    file_name: str = None
    file_path: str = None


@api_router.get("/list_files")
def list_files_api(filters: str = {}, pagination_data_required: bool = False):
    try:
        return list_files(
            filters=filters, pagination_data_required=pagination_data_required
        )
    except HTTPException as e:
        raise
    except Exception as e:
        return JSONResponse(
            status_code=500, content={"success": False, "error": str(e)}
        )


@api_router.post("/create_file")
def create_api(request: FileUploader):
    try:
        return create_file(request)
    except HTTPException as e:
        raise
    except Exception as e:
        return JSONResponse(
            status_code=500, content={"success": False, "error": str(e)}
        )


@api_router.post("/update_file")
def update_api(request: UpdateFile):
    try:
        return update_file(request)
    except HTTPException as e:
        raise
    except Exception as e:
        return JSONResponse(
            status_code=500, content={"success": False, "error": str(e)}
        )


@api_router.post("/upload_file")
async def upload_file(file: UploadFile = File(...)):
    try:
        file_path = UPLOAD_DIR / file.filename
        with open(file_path, "wb") as f:
            f.write(await file.read())

        file_url = f"http://localhost:8000/files/{file.filename}"
        return {"file_url": file_url}
    except Exception as e:
        return JSONResponse(content={"message": f"Error: {str(e)}"}, status_code=400)