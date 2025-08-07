import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def clean_data(df):
    # Remove rows with missing values
    df = df.dropna()
    return df

def normalize_data(df):
    scaler = MinMaxScaler()
    normalized_df = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
    return normalized_df

def preprocess_health_data(df):
    # Fill missing values, normalize numeric columns
    df = df.fillna(df.mean(numeric_only=True))
    numeric_cols = ['heart_rate', 'blood_oxygen']
    df[numeric_cols] = (df[numeric_cols] - df[numeric_cols].mean()) / df[numeric_cols].std()
    return df