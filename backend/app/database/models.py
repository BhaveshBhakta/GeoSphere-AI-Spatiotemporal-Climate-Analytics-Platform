from sqlalchemy import Column, Integer, String, Float, DateTime
from app.database.connection import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import DateTime

from datetime import datetime

class WeatherHistory(Base):

    __tablename__ = "weather_history"

    id = Column(Integer, primary_key=True, index=True)

    city = Column(String)

    country = Column(String)

    temperature = Column(Float)

    humidity = Column(Float)

    rainfall = Column(Float)

    wind_speed = Column(Float)

    timestamp = Column(DateTime)


class RiskHistory(Base):

    __tablename__ = "risk_history"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    city = Column(
        String
    )

    risk_score = Column(
        Float
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )