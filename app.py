# app.py
from flask import Flask, render_template, request
import pickle
import pandas as pd
import mysql.connector

# Load model and features
model = pickle.load(open("churn_model.pkl", "rb"))
features = pickle.load(open("feature_columns.pkl", "rb"))

app = Flask(__name__)

# ✅ MySQL connection setup using PORT 3306
def save_to_mysql(input_data, prediction, confidence):
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",     # or "localhost"
            user="root",
            password="root",  # 🔁 Replace with your actual password
            database="churn_db",
            port=3306             # ✅ Set to 3306
        )
        cursor = conn.cursor()

        query = """
        INSERT INTO churn_predictions (SeniorCitizen, tenure, MonthlyCharges, Contract, PaymentMethod, InternetService, prediction, confidence)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            input_data['SeniorCitizen'],
            input_data['tenure'],
            input_data['MonthlyCharges'],
            input_data['Contract'],
            input_data['PaymentMethod'],
            input_data['InternetService'],
            prediction,
            confidence
        )

        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print("MySQL Error:", err)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    input_data = {
        'SeniorCitizen': int(request.form['SeniorCitizen']),
        'tenure': float(request.form['tenure']),
        'MonthlyCharges': float(request.form['MonthlyCharges']),
        'Contract': request.form['Contract'],
        'PaymentMethod': request.form['PaymentMethod'],
        'InternetService': request.form['InternetService']
    }

    # Add all expected feature columns with default 0
    data = {col: 0 for col in features}
    for key in ['SeniorCitizen', 'tenure', 'MonthlyCharges']:
        if key in data:
            data[key] = input_data[key]

    # Handle one-hot encoded categorical inputs
    categorical_inputs = [
        'Contract_' + input_data['Contract'],
        'PaymentMethod_' + input_data['PaymentMethod'],
        'InternetService_' + input_data['InternetService']
    ]
    for cat in categorical_inputs:
        if cat in data:
            data[cat] = 1

    # Convert to DataFrame
    input_df = pd.DataFrame([data])

    # Predict with confidence score
    proba = model.predict_proba(input_df)[0]
    prediction = model.predict(input_df)[0]
    confidence = round(max(proba) * 100, 2)

    # Save to MySQL
    save_to_mysql(input_data, int(prediction), confidence)

    # Display result
    if prediction == 1:
        result = f"⚠️ Customer is likely to churn with {confidence}% confidence."
    else:
        result = f"✅ Customer is not likely to churn. Confidence: {confidence}%."

    return render_template("index.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)
