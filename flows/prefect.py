from prefect import flow, task
from batch_dev.data_loader import load_stock_data
from train_dev.train_model import train_model

@task
def load_data():
    return load_stock_data("data/SPX.csv")

@task
def train(df):
    return train_model(df)

@flow
def full_pipeline():
    df = load_data()
    model = train(df)

if __name__ == "__main__":
    full_pipeline()