from app.agent.router import route_query

from app.agent.tools import (
    rag_tool,
    prediction_tool,
    weather_tool
)


def run_agent(question):

    route = route_query(question)

    print(f"Selected Route: {route}")

    if route == "prediction":

        return {
            "route": "prediction",
            "data": prediction_tool()
        }

    elif route == "weather":

        weather_data = weather_tool("Delhi")

        return {
            "route": "weather",
            "data": weather_data
        }

    else:

        return {
            "route": "rag",
            "answer": rag_tool(question)
        }