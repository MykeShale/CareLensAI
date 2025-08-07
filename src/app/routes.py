from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def home():
    data_path = os.path.join(os.path.dirname(__file__), '../../data/health_metrics.csv')
    df = pd.read_csv(data_path)
    latest = df.iloc[-1].to_dict()
    return render_template('index.html', data=latest)

if __name__ == '__main__':
    app.run(debug=True)