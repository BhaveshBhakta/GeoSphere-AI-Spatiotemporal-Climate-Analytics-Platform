from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.analytics import router as analytics_router
from app.routes.forecast import router as forecast_router
from app.routes.explain import router as explain_router
from app.routes.chat import router as chat_router
from app.routes.weather import router as weather_router
from app.routes.agent_chat import router as agent_router
from app.routes.risk import router as risk_router
from app.routes.risk_history import (router as risk_history_router)
from app.routes.report import (router as report_router)
from app.routes.upload import (router as upload_router)
from app.routes.upload_chat import (router as upload_chat_router)
from app.routes.compare import (router as compare_router)
from app.routes.alerts import (router as alerts_router)
from app.routes.insights import (router as insights_router)
from app.routes.forecast7 import (router as forecast7_router)
from app.routes.scenario import (router as scenario_router)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analytics_router)
app.include_router(forecast_router)
app.include_router(explain_router)
app.include_router(weather_router)
app.include_router(chat_router)
app.include_router(agent_router)
app.include_router(risk_router)
app.include_router(risk_history_router)
app.include_router(report_router)
app.include_router(upload_router)
app.include_router(upload_chat_router)
app.include_router(compare_router)
app.include_router(alerts_router)
app.include_router(insights_router)
app.include_router(forecast7_router)
app.include_router(scenario_router)

@app.get("/")
def home():
    return {"message": "ClimateGuard AI Backend Running"}