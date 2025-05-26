import pandas as pd
import pickle
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import mlflow
import os

@flow(log_prints=True)
def train_model(file_path="data/SPX.csv", alpha=1.0):
    os.makedirs("ML_models", exist_ok=True)
    df = pd.read_csv(file_path)

    df['Target'] = df['Close'].pct_change().shift(-1)
    df = df.dropna()

    X = df[['Open', 'High', 'Low', 'Close', 'Volume']]
    y = df['Target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    mlflow.set_tracking_uri("http://mlflow:5000")
    mlflow.set_experiment("sp500_regression")

    with mlflow.start_run():

        model = Ridge(alpha=alpha)
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        print(f"Test MSE: {mse:.5f}")


        mlflow.log_param("alpha", alpha)
        mlflow.log_metric("mse", mse)
        mlflow.sklearn.log_model(model, "model")

        with open("ML_models/ridge_model.pkl", "wb") as f:
            pickle.dump(model, f)

        print(f"✅ Model getraind (alpha={alpha})")
        print(f"Train MSE: {mse_train:.6f}")
        print(f"Test  MSE: {mse_test:.6f}")

if __name__ == "__main__":
    train_model()