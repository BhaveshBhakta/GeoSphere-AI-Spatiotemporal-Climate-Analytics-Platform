from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.analytics import router as analytics_router
from app.routes.forecast import router as forecast_router
from app.routes.explain import router as explain_router

from app.routes.weather import router as weather_router

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


@app.get("/")
def home():
    return {"message": "ClimateGuard AI Backend Running"}