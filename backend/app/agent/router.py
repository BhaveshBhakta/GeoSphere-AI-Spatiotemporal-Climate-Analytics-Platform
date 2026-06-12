def route_query(question):

    q = question.lower()

    if any(
        word in q
        for word in [
            "predict",
            "forecast",
            "tomorrow",
            "future"
        ]
    ):
        return "prediction"

    if any(
        word in q
        for word in [
            "history",
            "trend",
            "over time"
        ]
    ):
        return "analytics"

    if any(
        word in q
        for word in [
            "temperature",
            "humidity",
            "rainfall",
            "weather"
        ]
    ):
        return "weather"

    return "rag"