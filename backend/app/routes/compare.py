from fastapi import APIRouter

from app.agent.comparison_tool import (
    compare_cities
)

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

    data = compare_cities(
        city1,
        city2
    )

    analysis = compare_city_analysis(
        city1,
        city2
    )

    return {

        "city1": city1,

        "city2": city2,

        "weather1":
        data["weather1"],

        "weather2":
        data["weather2"],

        "risk1":
        data["risk1"],

        "risk2":
        data["risk2"],

        "analysis":
        analysis

    }