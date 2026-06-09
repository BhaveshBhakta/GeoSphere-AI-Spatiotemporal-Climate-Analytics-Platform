import requests
from datetime import datetime
from app.database.connection import SessionLocal
from app.database.models import WeatherHistory


def calculate_aqi_risk(pm25):
    if pm25 is None:
        return "Unknown"

    if pm25 <= 12:
        return "Good"

    elif pm25 <= 35:
        return "Moderate"

    elif pm25 <= 55:
        return "Unhealthy"

    else:
        return "Hazardous"


def get_weather_data(city: str):

    geocode_url = (
        f"https://geocoding-api.open-meteo.com/v1/search?"
        f"name={city}&count=1"
    )

    geo_response = requests.get(geocode_url).json()

    results = geo_response.get("results")

    if not results:
        return {"error": "City not found"}

    location = results[0]

    latitude = location["latitude"]
    longitude = location["longitude"]

    weather_url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}"
        f"&longitude={longitude}"
        f"&current=temperature_2m,relative_humidity_2m,rain,wind_speed_10m"
        f"&daily=temperature_2m_max"
        f"&forecast_days=7"
    )

    air_quality_url = (
        f"https://air-quality-api.open-meteo.com/v1/air-quality?"
        f"latitude={latitude}"
        f"&longitude={longitude}"
        f"&current=pm10,pm2_5,carbon_monoxide,nitrogen_dioxide"
    )

    weather_response = requests.get(weather_url).json()
    aqi_response = requests.get(air_quality_url).json()
    current = weather_response.get("current", {})
    air_current = aqi_response.get("current", {})
    daily = weather_response.get("daily", {})

    forecast = []

    dates = daily.get("time", [])
    temps = daily.get("temperature_2m_max", [])

    for i in range(len(dates)):
        forecast.append({
            "day": dates[i],
            "temp": temps[i]
        })


    db = SessionLocal()

    weather_entry = WeatherHistory(
        city=location["name"],

        country=location.get("country"),

        temperature=current.get("temperature_2m"),

        humidity=current.get("relative_humidity_2m"),

        rainfall=current.get("rain"),

        wind_speed=current.get("wind_speed_10m"),

        timestamp=datetime.utcnow()
    )

    db.add(weather_entry)

    db.commit()

    db.close()

    return {
        "city": location["name"],
        "country": location.get("country"),

        "latitude": latitude,
        "longitude": longitude,

        "temperature": current.get("temperature_2m"),

        "humidity": current.get("relative_humidity_2m"),

        "rainfall": current.get("rain"),

        "wind_speed": current.get("wind_speed_10m"),

        "pm10": air_current.get("pm10"),

        "pm25": air_current.get("pm2_5"),

        "carbon_monoxide": air_current.get("carbon_monoxide"),

        "nitrogen_dioxide": air_current.get("nitrogen_dioxide"),

        "aqi_risk": calculate_aqi_risk(
            air_current.get("pm2_5")
        ),

        "forecast": forecast
    }