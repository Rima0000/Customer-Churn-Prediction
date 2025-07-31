# 🔄 Customer Churn Prediction Web App

A Machine Learning-powered Flask web application that predicts whether a customer is likely to churn based on inputs like tenure, contract type, payment method, and more. It also displays a confidence score and logs predictions into a MySQL database.

## 🚀 Features

- Built using **Random Forest Classifier**
- Interactive web UI with confidence score
- Styled using HTML & CSS (with animations and colors)
- Real-time prediction with meaningful results
- MySQL database integration for storing predictions

## 🧠 Tech Stack

- Python (pandas, scikit-learn)
- Flask
- HTML/CSS (frontend UI)
- MySQL (prediction log storage)
- Jupyter Notebook (for model training)

## 📥 Inputs Accepted

- Senior Citizen (Yes/No)
- Tenure (in months)
- Monthly Charges (float)
- Contract Type (Month-to-month, One year, Two year)
- Payment Method (Electronic check, Mailed check, etc.)
- Internet Service (DSL, Fiber optic, No)

## 📤 Output

- Whether the customer is likely to churn
- Confidence score of the prediction
- Logs saved to MySQL database with input + prediction


## 🔗 Live Demo

👉 [Click here to view the demo](https://your-live-demo-link.com)

## 💡 Future Work

- Add user authentication
- Deploy on cloud platforms (Azure, Render, Heroku)
- Include more features from the dataset
