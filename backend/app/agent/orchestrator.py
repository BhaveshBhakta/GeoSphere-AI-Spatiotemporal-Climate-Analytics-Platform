from app.agent.intent_classifier import (
    classify_intent
)

from app.agent.explainer import (
    generate_explanation
)

from app.agent.tools import (
    weather_tool,
    prediction_tool,
    rag_tool,
    risk_tool
)

from app.agent.multi_tool_agent import (
    multi_tool_analysis
)

from app.agent.analytics_agent import (
    historical_analysis
)

def run_agent(
    question,
    city="Delhi"
):
    print("=" * 50)
    print("QUESTION:", question)
    print("CITY:", city)
    print("=" * 50)
    route = classify_intent(question)

    print(
        f"Selected Route: {route}"
    )

    if route == "weather":

        context = weather_tool(city)

        return {

            "route": route,

            "answer": generate_explanation(
                question,
                context
            )
        }

    elif route == "prediction":

        context = prediction_tool(city)

        return {

            "route": route,

            "answer": generate_explanation(
                question,
                context
            )
        }


    elif route == "risk":

        risk_data = risk_tool(city)

        context = f"""
City:
{risk_data['city']}

Overall Climate Risk Score:
{risk_data['overall_score']}/100

Heatwave Risk:
{risk_data['heatwave']['level']}

Air Quality Risk:
{risk_data['aqi']['level']}

Flood Risk:
{risk_data['flood']['level']}

Drought Risk:
{risk_data['drought']['level']}

Task:
Explain the climate risks.
Suggest precautions if needed.
"""

        return {

            "route": route,

            "answer": generate_explanation(
                question,
                context
            )
        }

    elif route == "analytics":

        return {

            "route": route,

            "answer": historical_analysis(
                question,
                city
            )
        }


    elif route == "analysis":

        return {

            "route": route,

            "answer": multi_tool_analysis(
                question,
                city
            )
        }

    elif route == "rag":

        return {

            "route": route,

            "answer": rag_tool(
                question
            )
        }


    return {

        "route": "unknown",

        "answer":
        "Unable to determine route."
    }