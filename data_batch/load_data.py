import pandas as pd

def load_stock_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=['Date'])
    df.sort_values('Date', inplace=True)
    df.fillna(method='ffill', inplace=True)
    df = df[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]
    return df
