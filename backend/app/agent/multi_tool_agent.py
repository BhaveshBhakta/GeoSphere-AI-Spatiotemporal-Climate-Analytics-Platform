from app.agent.tools import (
    weather_tool,
    prediction_tool,
    risk_tool,
    rag_tool
)

from app.agent.explainer import (
    generate_explanation
)


def multi_tool_analysis(
    question,
    city="Delhi"
):

    weather = weather_tool(city)

    prediction = prediction_tool(city)

    risk = risk_tool(city)

    climate_context = rag_tool(question)

    context = f"""
WEATHER DATA

{weather}


FORECAST DATA

{prediction}


RISK DATA

Overall Score:
{risk['overall_score']}

Heatwave:
{risk['heatwave']['level']}

AQI:
{risk['aqi']['level']}


CLIMATE KNOWLEDGE

{climate_context}
"""

    return generate_explanation(
        question,
        context
    )