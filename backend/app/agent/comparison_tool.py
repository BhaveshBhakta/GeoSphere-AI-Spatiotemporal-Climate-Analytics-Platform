from app.services.weather_service import (
    get_weather_data
)

from app.agent.tools import (
    risk_tool
)


def compare_cities(
    city1,
    city2
):

    weather1 = get_weather_data(
        city1
    )

    weather2 = get_weather_data(
        city2
    )

    risk1 = risk_tool(city1)

    risk2 = risk_tool(city2)

    return {

        "city1": city1,

        "city2": city2,

        "weather1": weather1,

        "weather2": weather2,

        "risk1": risk1,

        "risk2": risk2

    }