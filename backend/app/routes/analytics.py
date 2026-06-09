from fastapi import APIRouter

from app.database.connection import SessionLocal

from app.database.models import WeatherHistory

router = APIRouter()


@router.get("/history/{city}")
def get_city_history(city: str):

    db = SessionLocal()

    records = (
        db.query(WeatherHistory)
        .filter(WeatherHistory.city == city)
        .all()
    )

    db.close()

    response = []

    for record in records:

        response.append({
            "temperature": record.temperature,
            "humidity": record.humidity,
            "rainfall": record.rainfall,
            "wind_speed": record.wind_speed,
            "timestamp": record.timestamp
        })

    return response