from fastapi import APIRouter

from app.agent.insights_agent import (
    generate_insights
)

router = APIRouter()


@router.get(
    "/insights/{city}"
)
def get_insights(
    city: str
):

    return {
        "insights":
        generate_insights(city)
    }