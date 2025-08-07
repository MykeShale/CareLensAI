import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest

def test_anomaly_detection():
    # Simulate health data for testing
    data = {
        'heart_rate': np.random.randint(60, 100, 100),
        'blood_oxygen': np.random.randint(90, 100, 100)
    }
    df = pd.DataFrame(data)

    # Train an anomaly detection model
    model = IsolationForest(contamination=0.1)
    df['anomaly'] = model.fit_predict(df[['heart_rate', 'blood_oxygen']])

    # Check if anomalies are labeled correctly
    assert df['anomaly'].value_counts().get(-1, 0) > 0, "No anomalies detected"
    assert df['anomaly'].value_counts().get(1, 0) > 0, "No normal data detected"

    # Check the shape of the dataframe
    assert df.shape[0] == 100, "Dataframe shape mismatch"
    assert 'anomaly' in df.columns, "Anomaly column not found in dataframe"