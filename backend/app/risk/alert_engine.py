def generate_alerts(
    risk_data
):

    alerts = []

    if (
        risk_data["heatwave"]["level"]
        in ["High", "Extreme"]
    ):

        alerts.append({

            "type":
            "Heatwave",

            "severity":
            risk_data["heatwave"]["level"],

            "message":
            "Avoid prolonged outdoor exposure."
        })

    if (
        risk_data["aqi"]["level"]
        in ["High", "Extreme"]
    ):

        alerts.append({

            "type":
            "Air Quality",

            "severity":
            risk_data["aqi"]["level"],

            "message":
            "Wear a mask outdoors."
        })

    if (
        risk_data["flood"]["level"]
        in ["High", "Extreme"]
    ):

        alerts.append({

            "type":
            "Flood",

            "severity":
            risk_data["flood"]["level"],

            "message":
            "Monitor local flood advisories."
        })

    if (
        risk_data["drought"]["level"]
        in ["High", "Extreme"]
    ):

        alerts.append({

            "type":
            "Drought",

            "severity":
            risk_data["drought"]["level"],

            "message":
            "Conserve water resources."
        })

    return alerts