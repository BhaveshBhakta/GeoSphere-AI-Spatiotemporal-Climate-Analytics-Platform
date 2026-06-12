def route_query(question):

    q = question.lower()

    rag_keywords = [
        "global warming",
        "climate change",
        "greenhouse",
        "carbon dioxide",
        "co2",
        "sustainability",
        "renewable",
        "environment",
        "ipcc"
    ]

    weather_keywords = [
        "temperature",
        "humidity",
        "rainfall",
        "aqi",
        "weather",
        "hot",
        "cold"
    ]

    prediction_keywords = [
        "predict",
        "forecast",
        "tomorrow",
        "future",
        "next week"
    ]

    analytics_keywords = [
        "trend",
        "history",
        "historical",
        "over time",
        "past"
    ]

    risk_keywords = [
        "risk",
        "heatwave",
        "flood",
        "drought"
    ]

    if any(k in q for k in prediction_keywords):
        return "prediction"

    if any(k in q for k in analytics_keywords):
        return "analytics"

    if any(k in q for k in risk_keywords):
        return "risk"

    if any(k in q for k in weather_keywords):
        return "weather"

    if any(k in q for k in rag_keywords):
        return "rag"

    return "rag"