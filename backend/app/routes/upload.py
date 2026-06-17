import os
import shutil

from fastapi import (
    APIRouter,
    UploadFile,
    File
)

from app.rag.upload_ingest import (
    ingest_uploaded_pdf
)

router = APIRouter()


@router.post("/upload-pdf")
async def upload_pdf(
    file: UploadFile = File(...)
):

    os.makedirs(
        "uploads",
        exist_ok=True
    )

    file_path = (
        f"uploads/{file.filename}"
    )

    with open(
        file_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    chunks = ingest_uploaded_pdf(
        file_path
    )

    return {

        "message":
        "Upload successful",

        "filename":
        file.filename,

        "chunks":
        chunks

    }