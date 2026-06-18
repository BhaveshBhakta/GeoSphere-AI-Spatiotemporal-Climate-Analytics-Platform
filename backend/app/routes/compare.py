from fastapi import APIRouter

from app.agent.comparison_agent import (
    compare_city_analysis
)

router = APIRouter()


@router.get(
    "/compare/{city1}/{city2}"
)
def compare(
    city1: str,
    city2: str
):

    return {

        "answer":
        compare_city_analysis(
            city1,
            city2
        )
    }