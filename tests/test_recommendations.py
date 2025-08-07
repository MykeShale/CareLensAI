import pytest
from src.recommendations import generate_recommendations

def test_generate_recommendations_normal():
    user_data = {
        'heart_rate': 75,
        'blood_oxygen': 98,
        'activity_level': 'moderate'
    }
    recommendations = generate_recommendations(user_data)
    assert isinstance(recommendations, list)
    assert len(recommendations) > 0

def test_generate_recommendations_high_heart_rate():
    user_data = {
        'heart_rate': 120,
        'blood_oxygen': 95,
        'activity_level': 'high'
    }
    recommendations = generate_recommendations(user_data)
    assert "Consult a doctor" in recommendations

def test_generate_recommendations_low_blood_oxygen():
    user_data = {
        'heart_rate': 70,
        'blood_oxygen': 85,
        'activity_level': 'low'
    }
    recommendations = generate_recommendations(user_data)
    assert "Increase oxygen intake" in recommendations

def test_generate_recommendations_inactive():
    user_data = {
        'heart_rate': 70,
        'blood_oxygen': 97,
        'activity_level': 'low'
    }
    recommendations = generate_recommendations(user_data)
    assert "Increase physical activity" in recommendations