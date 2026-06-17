from app.agent.tools import (
    analytics_tool,
    risk_tool
)

from app.agent.explainer import (
    generate_explanation
)


def historical_analysis(
    question,
    city="Delhi"
):

    history = analytics_tool(
        city
    )

    risk = risk_tool(
        city
    )

    context = f"""
HISTORICAL DATA

{history}


CURRENT RISK

Overall Risk:
{risk['overall_score']}/100

Heatwave:
{risk['heatwave']['level']}

AQI:
{risk['aqi']['level']}
"""

    return generate_explanation(
        question,
        context
    )