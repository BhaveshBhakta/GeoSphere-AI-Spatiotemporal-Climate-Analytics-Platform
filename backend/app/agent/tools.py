from app.rag.climate_assistant import ask_climate_assistant

from app.ml.forecasting.predict import predict_temperature

from app.ml.forecasting.predict_xgboost import predict_xgboost

from app.database.connection import SessionLocal

from app.database.models import WeatherHistory

from app.services.weather_service import get_weather_data


def rag_tool(question):

    return ask_climate_assistant(question)


def prediction_tool(city="Delhi"):

    weather = get_weather_data(city)

    lstm_pred = predict_temperature()

    xgb_pred = predict_xgboost()

    return f"""
City: {city}

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

def weather_tool(city="Delhi"):

    weather = get_weather_data(city)

    return f"""
City: {weather.get('city')}

Temperature: {weather.get('temperature')} °C

Humidity: {weather.get('humidity')} %

Rainfall: {weather.get('rainfall')} mm

Wind Speed: {weather.get('wind_speed')} km/h

PM2.5: {weather.get('pm25')}

AQI Risk: {weather.get('aqi_risk')}
"""


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

    return records