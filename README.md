# Diabetes Prediction ML Model - Logistic Regression 🩺

A Machine Learning based Diabetes Prediction API built using **Logistic Regression** and deployed using **Flask**.

This project predicts whether a person is likely to have diabetes based on health-related input features using a trained Machine Learning model.

---

## 🚀 Live API

API Deployment Link:

https://diabetes-prediction-ml-model-ilnq.onrender.com

API Status:

```
Welcome to the Diabetes Prediction API! Send POST requests to /predict with your data.
```

---

# 📌 Project Overview

This project uses a **Logistic Regression Machine Learning algorithm** to classify whether a person has diabetes or not.

The trained model is saved using **Joblib** and integrated with a Flask REST API.

The API receives user health information in JSON format and returns the prediction result.

---

# 🛠️ Technologies Used

- Python
- Flask
- Scikit-learn
- Logistic Regression
- Pandas
- NumPy
- Joblib
- Gunicorn
- Render Deployment

---

# 📂 Project Structure

```
Diabetes-Prediction-ML-Model
│
├── app.py
│
├── logistic_regression_model.joblib
│
├── requirements.txt
│
└── README.md
```

---

# 🧠 Machine Learning Model

## Algorithm Used

```
Logistic Regression
```

## Why Logistic Regression?

Logistic Regression is used because this is a binary classification problem.

The model predicts two classes:

```
0 → No Diabetes

1 → Diabetes
```

---

# 📊 Input Features

The model uses the following input parameters:

| Feature | Description |
|---------|-------------|
| Pregnancies | Number of pregnancies |
| Glucose | Blood glucose level |
| BloodPressure | Blood pressure value |
| SkinThickness | Skin thickness measurement |
| Insulin | Insulin level |
| BMI | Body Mass Index |
| DiabetesPedigreeFunction | Diabetes history value |
| Age | Person age |

---

# 🔥 API Endpoint

## Predict Diabetes

### Request Type

```
POST
```

### Endpoint

```
/predict
```

Example:

```
https://diabetes-prediction-ml-model-ilnq.onrender.com/predict
```

---

# 📥 Request Body

Send JSON data:

```json
{
    "Pregnancies": 2,
    "Glucose": 120,
    "BloodPressure": 70,
    "SkinThickness": 20,
    "Insulin": 80,
    "BMI": 25,
    "DiabetesPedigreeFunction": 0.5,
    "Age": 30
}
```

---

# 📤 Response

Example Response:

```json
{
    "prediction": "No Diabetes"
}
```

or

```json
{
    "prediction": "Diabetes"
}
```

---

# ⚙️ Run Project Locally

## Clone Repository

```bash
git clone <your-github-repository-url>
```

Move into project folder:

```bash
cd Diabetes-Prediction-ML-Model
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Flask Application

```bash
python app.py
```

Application runs on:

```
http://127.0.0.1:5000
```

---

# 📦 requirements.txt

```
flask
pandas
numpy
joblib
scikit-learn
gunicorn
```

---

# 🚀 Deployment

The Flask API is deployed using:

```
Render
```

Production server:

```
Gunicorn
```

Start command:

```
gunicorn app:app
```

---

# 🔄 Workflow

```
User Input
     |
     |
Flask API (/predict)
     |
     |
Machine Learning Model
     |
     |
Logistic Regression Prediction
     |
     |
Prediction Result
```

---

# ⚠️ Disclaimer

This project is created for educational purposes only.

The prediction output should not be considered as a medical diagnosis.

---

# 👩‍💻 Author

**Padmavathi**

Machine Learning | Flask API | Data Analytics
