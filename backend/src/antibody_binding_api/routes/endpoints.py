from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from ..utils.general import save_upload_file
from ..crud.operations import process_file
import os

router = APIRouter()

@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Invalid file format. Only CSV files are allowed.")
    
    try:
        file_location = f"temp/{file.filename}"
        save_upload_file(file, file_location)
        histogram_path, stats_path = process_file(file_location)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while processing the file: {str(e)}")
    
    return {"histogram": histogram_path, "statistics": stats_path}

@router.get("/download/{filename}")
async def download_file(filename: str):
    file_path = f"temp/{filename}"
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    
    return FileResponse(file_path)