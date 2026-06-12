from app.agent.intent_classifier import (
    classify_intent
)

from app.agent.explainer import (
    generate_explanation
)

from app.agent.tools import (
    weather_tool,
    prediction_tool,
    rag_tool
)


def run_agent(question):

    route = classify_intent(question)

    print(f"Selected Route: {route}")

    if route == "weather":

        context = weather_tool("Delhi")

        return {
            "answer": generate_explanation(
                question,
                context
            )
        }

    elif route == "prediction":

        context = prediction_tool()

        return {
            "answer": generate_explanation(
                question,
                context
            )
        }

    elif route == "rag":

        return {
            "answer": rag_tool(question)
        }

    return {
        "answer": "Unable to determine route."
    }