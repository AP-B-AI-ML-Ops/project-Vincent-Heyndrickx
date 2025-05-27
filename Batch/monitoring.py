import os
import pickle
import pandas as pd
import mlflow
from mlflow.tracking import MlflowClient
from sqlalchemy import create_engine
from sqlalchemy.dialects.postgresql import JSON
from evidently import Report
from evidently.presets import DataDriftPreset
from prefect import flow, task
from datetime import datetime

mlflow.set_tracking_uri("http://mlflow:5000")
client = MlflowClient()
MODEL_NAME = "sp500_regression"

DB_URI = "postgresql+psycopg://postgres:password@postgres:5432/postgres"
engine = create_engine(DB_URI)


@task(log_prints=True)
def load_data(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath)
    df = df.rename(columns={"Date": "date", "Close": "close"})
    df["date"] = pd.to_datetime(df["date"])
    df["return"] = df["close"].pct_change()
    return df.dropna()


@task(log_prints=True)
def save_to_db(df: pd.DataFrame):
    df.to_sql("batch_data", engine, if_exists="append", index=False)


@task(log_prints=True)
def load_model_and_vectorizer():
    version = client.get_latest_versions(MODEL_NAME, stages=["None"])[0]
    model = mlflow.pyfunc.load_model(version.source)
    with open("dv.pkl", "rb") as f:
        dv = pickle.load(f)
    return model, dv, version.run_id


@task(log_prints=True)
def predict(df: pd.DataFrame, model, dv, run_id: str) -> pd.DataFrame:
    features = df[["Open", "High", "Low", "Close", "Volume"]]
    transformed = dv.transform(features.to_dict(orient="records"))
    df["predicted_return"] = model.predict(transformed)
    df["run_id"] = run_id
    return df


@task(log_prints=True)
def run_drift_report():
    query_ref = "SELECT * FROM batch_data ORDER BY date ASC LIMIT 100"
    query_cur = "SELECT * FROM batch_data ORDER BY date DESC LIMIT 100"
    ref = pd.read_sql(query_ref, engine)
    cur = pd.read_sql(query_cur, engine)

    report = Report(metrics=[DataDriftPreset()])
    report.run(reference_data=ref, current_data=cur)
    result = report.as_dict()

    records = []
    now = datetime.now()
    for metric in result["metrics"]:
        records.append({"run_time": now, "metric_name": metric["metric_id"], "value": metric["value"]})
    pd.DataFrame(records).to_sql("evidently_metrics", engine, if_exists="replace", index=False, dtype={"value": JSON})


@flow(log_prints=True)
def run_batch_pipeline():
    df = load_data("data/daily.csv")
    save_to_db(df)
    model, dv, run_id = load_model_and_vectorizer()
    pred_df = predict(df, model, dv, run_id)
    pred_df.to_csv("data/predictions.csv", index=False)
    run_drift_report()


if __name__ == "__main__":
    run_batch_pipeline.serve(
        name="batch-pipeline",
        parameters={}
    )
