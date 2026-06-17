from app.rag.climate_assistant import ask_climate_assistant
from app.ml.forecasting.predict import predict_temperature
from app.ml.forecasting.predict_xgboost import predict_xgboost
from app.database.connection import SessionLocal
from app.database.models import WeatherHistory
from app.services.weather_service import get_weather_data
from app.risk.risk_engine import (
    calculate_heatwave_risk,
    calculate_aqi_risk,
    calculate_flood_risk,
    calculate_drought_risk,
    overall_risk_score
)
from app.risk.store_risk import (
    save_risk_score
)


# RAG TOOL

def rag_tool(question):

    return ask_climate_assistant(question)


# WEATHER TOOL

def weather_tool(city="Delhi"):

    weather = get_weather_data(city)

    return f"""
City: {weather.get('city')}

Temperature:
{weather.get('temperature')} °C

Humidity:
{weather.get('humidity')} %

Rainfall:
{weather.get('rainfall')} mm

Wind Speed:
{weather.get('wind_speed')} km/h

PM2.5:
{weather.get('pm25')}

AQI Risk:
{weather.get('aqi_risk')}

Task:
Explain current weather conditions and possible causes.
"""
    
# PREDICTION TOOL

def prediction_tool(city="Delhi"):

    weather = get_weather_data(city)

    lstm_pred = predict_temperature()

    xgb_pred = predict_xgboost()

    return f"""
City:
{city}

Current Temperature:
{weather.get('temperature')} °C

LSTM Forecast:
{round(lstm_pred, 2)} °C

XGBoost Forecast:
{round(xgb_pred, 2)} °C

Forecast Period:
Next Day

Task:
Explain whether temperature is likely to increase or decrease.
Mention uncertainty if the models disagree.
"""
    
# ANALYTICS TOOL
def analytics_tool(city):

    db = SessionLocal()

    records = (

        db.query(WeatherHistory)

        .filter(
            WeatherHistory.city == city
        )

        .all()

    )

    db.close()

    if not records:

        return "No historical data available."

    temperatures = [
        r.temperature
        for r in records
    ]

    humidity = [
        r.humidity
        for r in records
    ]

    rainfall = [
        r.rainfall
        for r in records
    ]

    avg_temp = (
        sum(temperatures)
        / len(temperatures)
    )

    avg_humidity = (
        sum(humidity)
        / len(humidity)
    )

    avg_rainfall = (
        sum(rainfall)
        / len(rainfall)
    )

    return f"""
City:
{city}

Historical Records:
{len(records)}

Average Temperature:
{avg_temp:.2f} °C

Average Humidity:
{avg_humidity:.2f} %

Average Rainfall:
{avg_rainfall:.2f} mm
"""

# RISK TOOL

def risk_tool(city="Delhi"):

    weather = get_weather_data(city)

    heatwave = calculate_heatwave_risk(
        weather["temperature"]
    )

    aqi = calculate_aqi_risk(
        weather["aqi_risk"]
    )

    flood = calculate_flood_risk(
        weather["rainfall"]
    )

    drought = calculate_drought_risk(
        weather["rainfall"],
        weather["humidity"]
    )

    overall = overall_risk_score(
        heatwave,
        flood,
        drought,
        aqi
    )

    save_risk_score(
        city,
        overall
    )

    return {

        "city": city,

        "overall_score": overall,

        "weather": weather,

        "heatwave": heatwave,

        "aqi": aqi,

        "flood": flood,

        "drought": drought

    }