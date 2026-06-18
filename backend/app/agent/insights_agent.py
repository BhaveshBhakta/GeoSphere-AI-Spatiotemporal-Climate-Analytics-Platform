from app.agent.tools import (
    weather_tool,
    prediction_tool,
    risk_tool
)

from app.agent.explainer import (
    generate_explanation
)


def generate_insights(
    city="Delhi"
):

    weather = weather_tool(city)

    prediction = prediction_tool(city)

    risk = risk_tool(city)

    context = f"""
WEATHER

{weather}

FORECAST

{prediction}

RISK

Overall Score:
{risk['overall_score']}

Heatwave:
{risk['heatwave']['level']}

AQI:
{risk['aqi']['level']}

Flood:
{risk['flood']['level']}

Drought:
{risk['drought']['level']}
"""

    question = """
Generate:

1. Climate Insights
2. Recommendations

Use bullet points.

Keep under 200 words.
"""

    return generate_explanation(
        question,
        context
    )