from datetime import date

from sqlalchemy import func

from app.database.connection import SessionLocal
from app.database.models import RiskHistory


def save_risk_score(
    city,
    score
):

    db = SessionLocal()

    existing_entry = (

        db.query(RiskHistory)

        .filter(
            RiskHistory.city == city
        )

        .filter(
            func.date(
                RiskHistory.created_at
            ) == date.today()
        )

        .first()

    )

    if existing_entry:

        db.close()

        return

    risk = RiskHistory(

        city=city,

        risk_score=score

    )

    db.add(risk)

    db.commit()

    db.close()