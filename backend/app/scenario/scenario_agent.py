from app.services.weather_service import (
    get_weather_data
)

from app.scenario.scenario_engine import (
    apply_scenario
)

from app.agent.explainer import (
    generate_explanation
)


def analyze_scenario(

    city,

    temp_change,

    rainfall_change,

    humidity_change

):

    current = get_weather_data(
        city
    )

    future = apply_scenario(

        current,

        temp_change,

        rainfall_change,

        humidity_change

    )

    context = f"""
Current Conditions

Temperature:
{current['temperature']}

Rainfall:
{current['rainfall']}

Humidity:
{current['humidity']}


Scenario Conditions

Temperature:
{future['temperature']}

Rainfall:
{future['rainfall']}

Humidity:
{future['humidity']}
"""

    question = """
Analyze this climate scenario.

Explain:

1. Climate impacts
2. Risks
3. Recommendations

Use bullet points.
"""

    return generate_explanation(
        question,
        context
    )