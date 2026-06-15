from fastapi import APIRouter
from pydantic import BaseModel

from app.agent.orchestrator import run_agent

router = APIRouter()


class AgentRequest(BaseModel):
    question: str
    city: str


@router.post("/agent-chat")
def agent_chat(request: AgentRequest):

    response = run_agent(
        request.question,
        request.city
    )

    return response