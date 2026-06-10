from fastapi import APIRouter

from app.ml.forecasting.predict import (
    predict_temperature
)

from app.ml.forecasting.predict_xgboost import (
    predict_xgboost
)

router = APIRouter()


@router.get("/predict")
def predict():

    lstm_prediction = predict_temperature()

    xgboost_prediction = predict_xgboost()

    return {
        "lstm_prediction": lstm_prediction,
        "xgboost_prediction": xgboost_prediction
    }