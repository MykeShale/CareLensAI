from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.ensemble import IsolationForest

def evaluate_model(df):
    X = df[['heart_rate', 'blood_oxygen']]
    y = df['anomaly'].apply(lambda x: 1 if x == 'Anomaly' else 0)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = IsolationForest(contamination=0.1, random_state=42)
    model.fit(X_train)
    y_pred = model.predict(X_test)
    y_pred = [1 if x == -1 else 0 for x in y_pred]
    print(classification_report(y_test, y_pred))