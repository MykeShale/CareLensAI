import pandas as pd
import numpy as np
from src.preprocessing import clean_data, normalize_data

def test_clean_data():
    # Simulate some raw data
    raw_data = pd.DataFrame({
        'heart_rate': [70, 80, None, 90, 100],
        'blood_oxygen': [95, 96, 97, None, 99],
        'activity_level': ['low', 'moderate', 'high', 'low', None]
    })
    
    cleaned_data = clean_data(raw_data)
    
    # Check if NaN values are handled
    assert cleaned_data.isnull().sum().sum() == 0, "Cleaned data should not contain NaN values"

def test_normalize_data():
    # Simulate some data
    data = pd.DataFrame({
        'heart_rate': [60, 70, 80, 90, 100],
        'blood_oxygen': [90, 92, 94, 96, 98]
    })
    
    normalized_data = normalize_data(data)
    
    # Check if the normalized data is within the expected range
    assert (normalized_data['heart_rate'].min() >= 0 and normalized_data['heart_rate'].max() <= 1), "Heart rate normalization failed"
    assert (normalized_data['blood_oxygen'].min() >= 0 and normalized_data['blood_oxygen'].max() <= 1), "Blood oxygen normalization failed"