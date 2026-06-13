def calculate_heatwave_risk(temp):

    if temp >= 42:
        return {
            "score": 100,
            "level": "Extreme"
        }

    elif temp >= 38:
        return {
            "score": 75,
            "level": "High"
        }

    elif temp >= 34:
        return {
            "score": 50,
            "level": "Moderate"
        }

    return {
        "score": 20,
        "level": "Low"
    }


def calculate_aqi_risk(aqi):

    if aqi == "Hazardous":

        return {
            "score": 100,
            "level": "Extreme"
        }

    elif aqi == "Unhealthy":

        return {
            "score": 75,
            "level": "High"
        }

    elif aqi == "Moderate":

        return {
            "score": 50,
            "level": "Moderate"
        }

    return {
        "score": 20,
        "level": "Low"
    }


def calculate_flood_risk(rainfall):

    if rainfall >= 50:

        return {
            "score": 100,
            "level": "Extreme"
        }

    elif rainfall >= 20:

        return {
            "score": 70,
            "level": "High"
        }

    elif rainfall >= 10:

        return {
            "score": 40,
            "level": "Moderate"
        }

    return {
        "score": 10,
        "level": "Low"
    }


def calculate_drought_risk(
    rainfall,
    humidity
):

    if rainfall == 0 and humidity < 40:

        return {
            "score": 90,
            "level": "High"
        }

    elif humidity < 50:

        return {
            "score": 60,
            "level": "Moderate"
        }

    return {
        "score": 20,
        "level": "Low"
    }

def overall_risk_score(
    heatwave,
    flood,
    drought,
    aqi
):

    score = (

        heatwave["score"] * 0.35 +

        aqi["score"] * 0.35 +

        flood["score"] * 0.15 +

        drought["score"] * 0.15

    )

    return round(score)