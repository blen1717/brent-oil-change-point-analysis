import pandas as pd
import numpy as np

def load_data(filepath):
    df = pd.read_csv(filepath)
    df['Date'] = pd.to_datetime(df['Date'], format='mixed')
    df = df.sort_values('Date').reset_index(drop=True)
    df['Log_Return'] = np.log(df['Price']) - np.log(df['Price'].shift(1))
    df = df.dropna()
    return df

def load_events(filepath):
    df = pd.read_csv(filepath)
    df['Date'] = pd.to_datetime(df['Date'])
    return df
