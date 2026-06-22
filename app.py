import joblib
import pandas as pd
from flask import Flask, request, jsonify

# Load the trained model and the scaler
model = joblib.load('logistic_regression_model.joblib')
scaler = joblib.load('scaler.joblib')

# Initialise the Flask application
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from the request
        data = request.get_json(force=True)

        # Convert dictionary to DataFrame, ensuring correct column order
        feature_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
        input_df = pd.DataFrame([data], columns=feature_names)
        
        # Scale the input data using the loaded scaler
        input_scaled = scaler.transform(input_df)

        # Make prediction
        prediction = model.predict(input_scaled)
        probability = model.predict_proba(input_scaled)[:, 1]

        # Return the prediction and probability
        return jsonify({
            'prediction': int(prediction[0]),
            'probability_of_diabetes': float(probability[0])
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Diabetes Prediction API! Send POST requests to /predict with your data."

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0', port=5000)
