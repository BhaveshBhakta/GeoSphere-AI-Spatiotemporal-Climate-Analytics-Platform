import torch
import numpy as np
import pandas as pd

from sklearn.preprocessing import MinMaxScaler

from app.database.connection import SessionLocal
from app.database.models import WeatherHistory

from app.ml.forecasting.lstm_model import LSTMModel


def predict_temperature():

    db = SessionLocal()

    records = db.query(WeatherHistory).all()

    db.close()

    temperatures = [r.temperature for r in records]

    df = pd.DataFrame(
        temperatures,
        columns=["temperature"]
    )

    scaler = MinMaxScaler()

    scaled_data = scaler.fit_transform(df)

    sequence_length = 5

    last_sequence = scaled_data[-sequence_length:]

    input_sequence = torch.tensor(
        [last_sequence],
        dtype=torch.float32
    )

    model = LSTMModel()

    model.load_state_dict(
        torch.load(
            "app/ml/forecasting/saved_models/lstm_model.pth"
        )
    )

    model.eval()

    with torch.no_grad():

        prediction = model(input_sequence)

    predicted_temp = scaler.inverse_transform(
        prediction.numpy()
    )

    return float(predicted_temp[0][0])