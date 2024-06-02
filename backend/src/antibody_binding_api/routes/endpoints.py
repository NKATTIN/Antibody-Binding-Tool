from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse
from ..utils.general import save_upload_file
from ..crud.operations import process_file

router = APIRouter()

@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_location = f"temp/{file.filename}"
    save_upload_file(file, file_location)
    histogram_path, stats_path = process_file(file_location)
    return {"histogram": histogram_path, "statistics": stats_path}

@router.get("/download/{filename}")
async def download_file(filename: str):
    file_path = f"temp/{filename}"
    return FileResponse(file_path)