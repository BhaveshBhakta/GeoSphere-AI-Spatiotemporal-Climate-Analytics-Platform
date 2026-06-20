from fastapi import APIRouter

from app.ml.forecasting.forecast_7day import (
    forecast_next_7_days
)

router = APIRouter()


@router.get(
    "/forecast7"
)
def forecast7():

    return {

        "forecast":
        forecast_next_7_days()

    }