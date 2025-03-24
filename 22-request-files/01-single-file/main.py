from typing import Annotated

from fastapi import FastAPI, File, UploadFile

app = FastAPI()


# Archivos pequeños carga todo en memoria
@app.post("/files/")
# async def create_file(file: Annotated[bytes, File()]):
# Carga opcional
# async def create_file(file: Annotated[bytes | None, File()] = None):
# Carga con metadatos adicionales
async def create_file(file: Annotated[bytes, File(description="A file read as bytes")]):
    return {"file_size": len(file)}


# Archivos grandes carga por stream
@app.post("/uploadfile/")
# async def create_upload_file(file: UploadFile):
# async def create_upload_file(file: UploadFile | None = None):  # Carga opcional
async def create_upload_file(
    file: Annotated[UploadFile, File(description="A file read as UploadFile")],
):  # Carga con metadatos adicionales
    return {"filename": file.filename}

# https://fastapi.tiangolo.com/tutorial/request-files/#file-parameters-with-uploadfile
