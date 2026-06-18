from fastapi import APIRouter

from app.agent.tools import (
    risk_tool
)

from app.risk.alert_engine import (
    generate_alerts
)

router = APIRouter()


@router.get(
    "/alerts/{city}"
)
def get_alerts(
    city: str
):

    risk_data = risk_tool(
        city
    )

    alerts = generate_alerts(
        risk_data
    )

    return {

        "city": city,

        "alerts": alerts
    }