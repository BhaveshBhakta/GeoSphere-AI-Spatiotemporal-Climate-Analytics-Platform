from app.agent.comparison_tool import (
    compare_cities
)

from app.agent.explainer import (
    generate_explanation
)


def compare_city_analysis(
    city1,
    city2
):

    data = compare_cities(
        city1,
        city2
    )

    context = f"""
City 1:
{city1}

Temperature:
{data['weather1']['temperature']}

AQI:
{data['weather1']['aqi_risk']}

Risk Score:
{data['risk1']['overall_score']}


City 2:
{city2}

Temperature:
{data['weather2']['temperature']}

AQI:
{data['weather2']['aqi_risk']}

Risk Score:
{data['risk2']['overall_score']}
"""

    question = f"""
Compare {city1} and {city2}.
Explain which city is currently safer.
Explain major climate differences.
"""

    return generate_explanation(
        question,
        context
    )