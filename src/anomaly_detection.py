import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies(df):
    model = IsolationForest(contamination=0.1, random_state=42)
    df['anomaly'] = model.fit_predict(df[['heart_rate', 'blood_oxygen']])
    df['anomaly'] = df['anomaly'].apply(lambda x: 'Anomaly' if x == -1 else 'Normal')
    return df

def main():
    # Example usage
    data = {
        'timestamp': pd.date_range(start='2023-10-01', periods=100, freq='T'),
        'heart_rate': [75, 80, 85, 90, 95, 100, 105, 110, 115, 120] * 10,
        'blood_oxygen': [95, 96, 97, 98, 99, 100, 95, 94, 93, 92] * 10
    }
    df = pd.DataFrame(data)
    anomalies = detect_anomalies(df)
    print(anomalies.head())

if __name__ == "__main__":
    main()