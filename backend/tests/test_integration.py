import os
from fastapi.testclient import TestClient
from src.antibody_binding_api.main import app

client = TestClient(app)

def test_upload_file():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    file_path = os.path.join(project_root, "example_data/input_data.csv")
    with open(file_path, "rb") as file:
        response = client.post("api/upload/", files={"file": file})
        assert response.status_code == 200
        assert "histogram" in response.json()
        assert "statistics" in response.json()

def test_invalid_file_upload():
    response = client.post("api/upload/", files={"file": ("invalid_file.txt", b"Not a CSV content")})
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid file format. Only CSV files are allowed."}

def test_download_file():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    file_path = os.path.join(project_root, "example_data/input_data.csv")
    with open(file_path, "rb") as file:
        client.post("api/upload/", files={"file": file})

    response = client.get("api/download/histogram.png")
    assert response.status_code == 200
    response = client.get("api/download/stats.csv")
    assert response.status_code == 200

def test_non_existent_file_download():
    response = client.get("api/download/non_existent_file.csv")
    assert response.status_code == 404
    assert response.json() == {"detail": "File not found"}