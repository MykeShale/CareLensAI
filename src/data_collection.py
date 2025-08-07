import pandas as pd
import numpy as np

def simulate_health_data(filepath='../data/health_metrics.csv', n=1000):
    """
    Simulate health data and save to a CSV file.
    
    Args:
        filepath (str): Path to the CSV file where data will be saved.
        n (int): Number of data points to simulate.
    """
    data = {
        'timestamp': pd.date_range(start='2023-10-01', periods=n, freq='T'),
        'heart_rate': np.random.randint(60, 100, n),
        'blood_oxygen': np.random.randint(90, 100, n),
        'activity_level': np.random.choice(['low', 'moderate', 'high'], n)
    }
    df = pd.DataFrame(data)
    df.to_csv(filepath, index=False)
    print(f"Simulated data saved to {filepath}")

if __name__ == "__main__":
    simulate_health_data()