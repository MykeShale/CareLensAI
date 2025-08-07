def generate_recommendations(heart_rate, blood_oxygen, activity_level):
    recommendations = []

    if heart_rate < 60:
        recommendations.append("Your heart rate is below normal. Consider consulting a healthcare professional.")
    elif heart_rate > 100:
        recommendations.append("Your heart rate is above normal. Engage in calming activities and consult a healthcare professional if it persists.")

    if blood_oxygen < 92:
        recommendations.append("Your blood oxygen level is low. Try to breathe deeply and seek fresh air. If it doesn't improve, consult a healthcare professional.")

    if activity_level == 'low':
        recommendations.append("Consider increasing your activity level. Aim for at least 30 minutes of moderate exercise most days of the week.")

    return recommendations

def personalized_health_advice(user_data):
    heart_rate = user_data.get('heart_rate')
    blood_oxygen = user_data.get('blood_oxygen')
    activity_level = user_data.get('activity_level')

    return generate_recommendations(heart_rate, blood_oxygen, activity_level)

def get_recommendation(row):
    if row['anomaly'] == 'Anomaly':
        if row['heart_rate'] > 0.5:
            return "High heart rate detected. Consider resting."
        elif row['blood_oxygen'] < -0.5:
            return "Low blood oxygen detected. Seek medical attention."
        else:
            return "Anomaly detected. Monitor your health."
    return "All metrics normal."

def add_recommendations(df):
    df['recommendation'] = df.apply(get_recommendation, axis=1)
    return df