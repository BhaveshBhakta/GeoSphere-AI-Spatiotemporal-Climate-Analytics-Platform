import torch
import numpy as np
import pandas as pd

from sklearn.preprocessing import MinMaxScaler

from app.database.connection import SessionLocal
from app.database.models import WeatherHistory

from app.ml.forecasting.lstm_model import LSTMModel


# DATABASE CONNECTION
db = SessionLocal()

records = db.query(WeatherHistory).all()

db.close()


# EXTRACT TEMPERATURES
temperatures = [r.temperature for r in records]

df = pd.DataFrame(temperatures, columns=["temperature"])


# NORMALIZATION
scaler = MinMaxScaler()

scaled_data = scaler.fit_transform(df)


# CREATE SEQUENCES
sequence_length = 5

X = []
y = []

for i in range(len(scaled_data) - sequence_length):

    X.append(
        scaled_data[i:i + sequence_length]
    )

    y.append(
        scaled_data[i + sequence_length]
    )

X = np.array(X)
y = np.array(y)


# CONVERT TO TENSORS
X_train = torch.tensor(
    X,
    dtype=torch.float32
)

y_train = torch.tensor(
    y,
    dtype=torch.float32
)


# MODEL
model = LSTMModel()

criterion = torch.nn.MSELoss()

optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001
)


# TRAINING LOOP
epochs = 100

for epoch in range(epochs):

    outputs = model(X_train)

    loss = criterion(outputs, y_train)

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()

    if (epoch + 1) % 10 == 0:

        print(
            f"Epoch [{epoch+1}/{epochs}], "
            f"Loss: {loss.item():.4f}"
        )


# SAVE MODEL
torch.save(
    model.state_dict(),
    "app/ml/forecasting/saved_models/lstm_model.pth"
)

print("LSTM model trained and saved")