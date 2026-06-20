import torch
import numpy as np
import pandas as pd

from sklearn.preprocessing import MinMaxScaler

from app.database.connection import SessionLocal
from app.database.models import WeatherHistory

from app.ml.forecasting.lstm_model import (
    LSTMModel
)


def forecast_next_7_days():

    db = SessionLocal()

    records = db.query(
        WeatherHistory
    ).all()

    db.close()

    if len(records) < 5:

        return []

    temperatures = [
        r.temperature
        for r in records
    ]

    df = pd.DataFrame(
        temperatures,
        columns=["temperature"]
    )

    scaler = MinMaxScaler()

    scaled_data = scaler.fit_transform(
        df
    )

    sequence_length = 5

    current_sequence = (
        scaled_data[-sequence_length:]
        .reshape(1, sequence_length, 1)
    )

    model = LSTMModel()

    model.load_state_dict(
        torch.load(
            "app/ml/forecasting/saved_models/lstm_model.pth"
        )
    )

    model.eval()

    predictions = []

    with torch.no_grad():

        for _ in range(7):

            tensor = torch.tensor(
                current_sequence,
                dtype=torch.float32
            )

            prediction = model(
                tensor
            )

            pred_value = (
                prediction.item()
            )

            predictions.append(
                pred_value
            )

            current_sequence = np.append(
                current_sequence[:, 1:, :],
                [[[pred_value]]],
                axis=1
            )

    predictions = scaler.inverse_transform(
        np.array(predictions)
        .reshape(-1, 1)
    )

    return (
        predictions
        .flatten()
        .tolist()
    )