from fastapi import APIRouter

from pydantic import BaseModel

from app.rag.uploaded_assistant import (
    ask_uploaded_pdf
)

router = APIRouter()


class Query(
    BaseModel
):
    question: str


@router.post(
    "/uploaded-chat"
)
def uploaded_chat(
    query: Query
):

    return {

        "answer":
        ask_uploaded_pdf(
            query.question
        )
    }