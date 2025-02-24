import joblib
import numpy as np

# Load trained models
dt_model = joblib.load("models/decision_tree.pkl")
svm_model = joblib.load("models/svm_model.pkl")

# Sample input for prediction (example)
sample_input = np.array([[5.1, 3.5, 1.4, 0.2]])  # Example input data

# Predict using Decision Tree model
dt_prediction = dt_model.predict(sample_input)
print(f"Decision Tree Prediction: {dt_prediction}")

# Predict using SVM model
svm_prediction = svm_model.predict(sample_input)
print(f"SVM Prediction: {svm_prediction}")
