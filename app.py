from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)

# Load your trained model (assuming you saved it using pickle)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the form data
    age = int(request.form['Age'])
    annual_income = float(request.form['Annual Income'])
    spending_score = int(request.form['Spending Score'])
    gender = request.form['gender']

    # Set gender columns
    if gender == 'Male':
        gender_male = 1
        gender_female = 0
    else:
        gender_male = 0
        gender_female = 1

    # Create the feature array
    features = np.array([[age, annual_income, spending_score, gender_female, gender_male]])

    # Predict the cluster
    prediction = model.predict(features)
    
    # You can customize the prediction_text based on your clusters or just return the cluster number
    prediction_text = f'Customer belongs to cluster {prediction[0]}'

    return render_template('home.html', prediction_text=prediction_text)

if __name__ == "__main__":
    app.run(debug=True)
