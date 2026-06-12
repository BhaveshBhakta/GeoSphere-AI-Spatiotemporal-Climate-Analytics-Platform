from app.rag.climate_assistant import ask_climate_assistant

from app.ml.forecasting.predict import predict_temperature

from app.ml.forecasting.predict_xgboost import predict_xgboost

from app.database.connection import SessionLocal

from app.database.models import WeatherHistory

from app.services.weather_service import get_weather_data


def rag_tool(question):

    return ask_climate_assistant(question)


def prediction_tool():

    return {
        "lstm": predict_temperature(),
        "xgboost": predict_xgboost()
    }


def weather_tool(city="Delhi"):

    return get_weather_data(city)


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