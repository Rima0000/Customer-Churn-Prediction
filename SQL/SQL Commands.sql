CREATE DATABASE IF NOT EXISTS churn_db;

USE churn_db;

CREATE TABLE IF NOT EXISTS churn_predictions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    SeniorCitizen INT,
    tenure FLOAT,
    MonthlyCharges FLOAT,
    Contract VARCHAR(50),
    PaymentMethod VARCHAR(50),
    InternetService VARCHAR(50),
    prediction INT,
    confidence FLOAT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

SELECT * FROM churn_predictions;
