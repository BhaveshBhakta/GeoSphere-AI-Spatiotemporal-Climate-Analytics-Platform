import requests


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

    weather_response = requests.get(weather_url).json()

    current = weather_response.get("current", {})
    daily = weather_response.get("daily", {})

    forecast = []

    dates = daily.get("time", [])
    temps = daily.get("temperature_2m_max", [])

    for i in range(len(dates)):
        forecast.append({
            "day": dates[i],
            "temp": temps[i]
        })

    return {
        "city": location["name"],
        "country": location.get("country"),
        "temperature": current.get("temperature_2m"),
        "humidity": current.get("relative_humidity_2m"),
        "rainfall": current.get("rain"),
        "wind_speed": current.get("wind_speed_10m"),
        "forecast": forecast
    }