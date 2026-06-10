import pandas as pd
import joblib

from xgboost import XGBRegressor

from app.database.connection import SessionLocal
from app.database.models import WeatherHistory


# DATABASE
db = SessionLocal()

records = db.query(WeatherHistory).all()

db.close()


# DATAFRAME
data = []

for r in records:

    data.append({
        "temperature": r.temperature,
        "humidity": r.humidity,
        "rainfall": r.rainfall,
        "wind_speed": r.wind_speed
    })

df = pd.DataFrame(data)


# FEATURES
X = df[[
    "humidity",
    "rainfall",
    "wind_speed"
]]

# TARGET
y = df["temperature"]


# MODEL
model = XGBRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=4
)

model.fit(X, y)


# SAVE MODEL
joblib.dump(
    model,
    "app/ml/forecasting/saved_models/xgboost_model.pkl"
)

print("XGBoost model trained and saved")