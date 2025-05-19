import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib
import mlflow
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset, DataQualityPreset

def train_model(df: pd.DataFrame):
    df['Return'] = df['Close'].pct_change()
    df['Target'] = df['Return'].shift(-1)
    df.dropna(inplace=True)

    X = df[['Open', 'High', 'Low', 'Close', 'Volume']]
    y = df['Target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = Ridge()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Test MSE: {mse:.5f}")

    joblib.dump(model, 'model.joblib')

    with mlflow.start_run():
        mlflow.log_metric("mse", mse)
        mlflow.sklearn.log_model(model, "model")

    # Evidently report
    report = Report(metrics=[DataDriftPreset(), DataQualityPreset()])
    report.run(reference_data=X_train, current_data=X_test)
    report.save_html("reports/evidently_report.html")

    return model