from fastapi import APIRouter

from pydantic import BaseModel

from app.rag.climate_assistant import (
    ask_climate_assistant
)

router = APIRouter()


class ChatRequest(BaseModel):

    question: str


@router.post("/chat")
def chat(request: ChatRequest):

    answer = ask_climate_assistant(
        request.question
    )

    return {
        "answer": answer
    }