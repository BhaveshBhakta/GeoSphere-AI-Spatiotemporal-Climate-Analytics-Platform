from fastapi import APIRouter
import joblib

router = APIRouter()


@router.get("/explain")
def explain_model():

    model = joblib.load(
        "app/ml/forecasting/saved_models/xgboost_model.pkl"
    )

    importance = model.feature_importances_

    features = [
        "humidity",
        "rainfall",
        "wind_speed"
    ]

    response = []

    for f, i in zip(features, importance):

        response.append({
            "feature": f,
            "importance": float(i)
        })

    return response