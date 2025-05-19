from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from prometheus_client import Counter, generate_latest
from fastapi.responses import Response

app = FastAPI()
model = joblib.load('model.joblib')
prediction_counter = Counter("stock_predictions", "Number of stock predictions made")

class StockInput(BaseModel):
    Open: float
    High: float
    Low: float
    Close: float
    Volume: float

@app.post("/predict")
def predict_stock(input: StockInput):
    features = np.array([[input.Open, input.High, input.Low, input.Close, input.Volume]])
    prediction = model.predict(features)[0]
    prediction_counter.inc()
    return {"predicted_return": prediction}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")