
# Run this in your local machine to start the API
# python app.py

from flask import Flask, jsonify
import pandas as pd
import numpy as np

app = Flask(name)
df = pd.read_csv('BrentOilPrices.csv')
df['Date'] = pd.to_datetime(df['Date'], format='mixed')
df['Log_Return'] = np.log(df['Price']) - np.log(df['Price'].shift(1))
df = df.dropna()

@app.route('/api/prices')
def get_prices():
    return jsonify({
        'dates': df['Date'].dt.strftime('%Y-%m-%d').tolist(),
        'prices': df['Price'].tolist(),
        'log_returns': df['Log_Return'].tolist()
    })

if name == 'main':
    app.run(debug=True, port=5000)
