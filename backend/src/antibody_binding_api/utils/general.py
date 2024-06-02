import os
from fastapi import UploadFile

def save_upload_file(upload_file: UploadFile, destination: str) -> str:
    os.makedirs(os.path.dirname(destination), exist_ok=True)
    with open(destination, "wb+") as file_object:
        file_object.write(upload_file.file.read())
    return destination