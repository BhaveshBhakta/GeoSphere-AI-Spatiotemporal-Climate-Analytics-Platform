import pandas as pd
import joblib

from app.database.connection import SessionLocal
from app.database.models import WeatherHistory


def predict_xgboost():

    model = joblib.load(
        "app/ml/forecasting/saved_models/xgboost_model.pkl"
    )

    db = SessionLocal()

    latest = (
        db.query(WeatherHistory)
        .order_by(WeatherHistory.id.desc())
        .first()
    )

    db.close()

    input_data = pd.DataFrame([{
        "humidity": latest.humidity,
        "rainfall": latest.rainfall,
        "wind_speed": latest.wind_speed
    }])

    prediction = model.predict(input_data)

    return float(prediction[0])