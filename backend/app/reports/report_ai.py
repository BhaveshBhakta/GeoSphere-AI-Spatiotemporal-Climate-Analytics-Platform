from app.agent.explainer import (
    generate_explanation
)


def generate_report_summary(
    city,
    weather,
    prediction,
    risk
):

    context = f"""
City: {city}

Weather:
{weather}

Forecast:
{prediction}

Risk:
{risk}
"""

    question = """
Create a professional climate report.

Use EXACTLY this structure:

Current Weather
- point
- point

Forecast Insights
- point
- point

Risk Assessment
- point
- point

Recommendations
- point
- point

Conclusion
- short paragraph

Keep it under 250 words.

Do not use markdown symbols such as **, ##, or *.
Use plain text only.
"""

    return generate_explanation(
        question,
        context
    )