import pickle
import pandas as pd
from flask import Flask, request, jsonify, Response
from mlflow.tracking import MlflowClient
import mlflow
from prometheus_client import Counter, generate_latest

app = Flask("s&p500-api")

mlflow.set_tracking_uri("http://mlflow:5000")
client = MlflowClient("http://mlflow:5000")

REGISTERED_MODEL_NAME = "sp500_regression"

prediction_counter = Counter("stock_predictions_total", "Aantal stock predicties")

def load_vectorizer():
    with open("dv.pkl", "rb") as f:
        return pickle.load(f)

def load_latest_model():
    latest_version = client.get_latest_versions(REGISTERED_MODEL_NAME, stages=["None"])[0]
    return mlflow.pyfunc.load_model(latest_version.source)

dv = load_vectorizer()
model = load_latest_model()

@app.route("/predict", methods=["POST"])
def predict():
    try:
        input_data = request.get_json()
        df = pd.DataFrame([input_data])
        transformed = dv.transform(df.to_dict(orient="records"))
        prediction = model.predict(transformed)[0]
        prediction_counter.inc()
        return jsonify({"predicted_return": float(prediction)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype="text/plain")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
