from fastapi import (
    APIRouter
)

from app.scenario.scenario_agent import (
    analyze_scenario
)

router = APIRouter()


@router.get(
    "/scenario/{city}"
)
def scenario(

    city: str,

    temp_change: float = 0,

    rainfall_change: float = 0,

    humidity_change: float = 0

):

    return {

        "analysis":

        analyze_scenario(

            city,

            temp_change,

            rainfall_change,

            humidity_change

        )
    }