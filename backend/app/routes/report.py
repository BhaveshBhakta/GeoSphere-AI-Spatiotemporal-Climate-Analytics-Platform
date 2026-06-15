from fastapi import APIRouter

from app.reports.report_service import (
    create_climate_report
)

router = APIRouter()


@router.get(
    "/report/{city}"
)
def generate_report(city: str):

    filename = (
        create_climate_report(city)
    )

    return {
        "message":
        "Report generated",

        "file":
        filename
    }