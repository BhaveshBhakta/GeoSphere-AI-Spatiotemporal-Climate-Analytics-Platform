from sqlalchemy import Column, Integer, String, Float, DateTime

from app.database.connection import Base


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