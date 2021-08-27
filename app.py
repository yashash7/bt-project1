from flask import Flask, render_template, url_for, request, jsonify
import joblib
import os
import pickle
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

#app
app = Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/result", methods=['POST', 'GET'])
def result():
    cylinders = request.form["cylinders"]
    displacement = request.form["displacement"]
    horsepower = str(request.form["horsepower"])
    weight = request.form["weight"]
    acceleration = request.form["acceleration"]
    model_year = request.form["model_year"]
    origin = request.form["origin"]
    values = [[cylinders, displacement, horsepower, weight, acceleration, model_year, origin]]
    
    scaler_path = 'models/scaler.pkl'
    sc = None
    with open(scaler_path, 'rb') as f:
        sc = pickle.load(f)
    #values = sc.transform(values)
    values = pd.read_csv(values, na_values='?')
    return values

if __name__=="__main__":
    app.run(debug=True, port=5100)