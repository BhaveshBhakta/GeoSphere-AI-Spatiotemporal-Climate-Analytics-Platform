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


def run_agent(question, city="Delhi"):

    route = classify_intent(question)

    print(f"Selected Route: {route}")

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

        context = risk_tool(city)

        return {
            "route": route,
            "answer": generate_explanation(
                question,
                context
            )
        }

    elif route == "rag":

        return {
            "route": route,
            "answer": rag_tool(question)
        }

    return {
        "route": "unknown",
        "answer": "Unable to determine route."
    }