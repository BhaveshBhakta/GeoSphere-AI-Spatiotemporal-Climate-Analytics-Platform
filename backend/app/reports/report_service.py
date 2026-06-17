from app.services.weather_service import (
    get_weather_data
)

from app.agent.tools import (
    risk_tool,
    analytics_tool
)

from app.ml.forecasting.predict import (
    predict_temperature
)

from app.ml.forecasting.predict_xgboost import (
    predict_xgboost
)

from app.reports.report_generator import (
    generate_report
)

from app.reports.report_ai import (
    generate_report_summary
)


def create_climate_report(
    city="Delhi"
):

    # WEATHER DATA

    weather_data = get_weather_data(city)

    weather = f"""
Temperature:
{weather_data['temperature']} °C

Humidity:
{weather_data['humidity']} %

Rainfall:
{weather_data['rainfall']} mm

Wind Speed:
{weather_data['wind_speed']} km/h

PM2.5:
{weather_data['pm25']}

AQI Risk:
{weather_data['aqi_risk']}
"""

    # FORECAST DATA

    lstm_prediction = predict_temperature()

    xgb_prediction = predict_xgboost()

    forecast = f"""
Current Temperature:
{weather_data['temperature']} °C

LSTM Forecast:
{round(lstm_prediction, 2)} °C

XGBoost Forecast:
{round(xgb_prediction, 2)} °C
"""

    # RISK DATA

    risk_data = risk_tool(city)

    risk = f"""
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

"""
    # Historical 

    historical = analytics_tool(
        city
    )

    # AI SUMMARY

    summary = generate_report_summary(
        city,
        weather,
        forecast,
        risk,
        historical
    )
    # REPORT CONTENT

    report_data = {
        "City": city,
        "Current Weather": weather,
        "Forecast Analysis": forecast,
        "Risk Assessment": risk,
        "Historical Analytics": historical,
        "AI Climate Analysis": summary
    }


    filename = (
        f"{city}_Climate_Report.pdf"
    )

    generate_report(
        filename,
        report_data
    )

    return filename