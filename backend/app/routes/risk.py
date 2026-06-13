from fastapi import APIRouter

from app.agent.tools import risk_tool

router = APIRouter()


@router.get("/risk/{city}")
def get_risk(city: str):

    return {
        "risk_report": risk_tool(city)
    }