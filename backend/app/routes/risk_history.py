from fastapi import APIRouter
from app.database.connection import SessionLocal
from app.database.models import RiskHistory

router = APIRouter()

@router.get(
    "/risk-history/{city}"
)
def risk_history(city: str):

    db = SessionLocal()

    records = (

        db.query(RiskHistory)

        .filter(
            RiskHistory.city == city
        )

        .all()

    )

    db.close()

    return [

        {
            "date":
            r.created_at.strftime(
                "%d %b %H:%M"
            ),

            "risk_score":
            r.risk_score
        }

        for r in records

    ]