from flask import Flask, render_template, request, jsonify
import pyttsx3
import pandas as pd
import joblib

app = Flask(__name__)

# Load trained ML models (Replace with actual trained models)
decision_tree_model = joblib.load("models/decision_tree.pkl")
svm_model = joblib.load("models/svm_model.pkl")

# Load symptom severity data (Adjust path if necessary)
symptom_severity = pd.read_csv("MasterData/Symptom_severity.csv")

# Function for voice output
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    symptoms = request.form.get("symptoms")
    symptoms_list = [s.strip() for s in symptoms.split(",")]

    # Convert symptoms to model input (Dummy Encoding)
    symptom_vector = [1 if s in symptoms_list else 0 for s in symptom_severity["Symptom"]]

    # Predict using ML models
    decision_tree_prediction = decision_tree_model.predict([symptom_vector])[0]
    svm_prediction = svm_model.predict([symptom_vector])[0]

    # Select the most confident prediction (or average them)
    final_prediction = decision_tree_prediction if decision_tree_prediction == svm_prediction else "Uncertain"

    # Example responses (Replace with actual data)
    disease_info = {
        "Cervical spondylosis": {
            "description": [
                "Age-related wear and tear affecting spinal disks in the neck.",
                "Disks dehydrate and shrink.",
                "Signs of osteoarthritis develop.",
                "Bone spurs may form."
            ],
            "precautions": [
                "Use heating pad or cold pack.",
                "Exercise regularly.",
                "Take OTC pain relievers.",
                "Consult a doctor if pain persists."
            ]
        }
    }

    response = disease_info.get(final_prediction, {"description": ["Unknown disease"], "precautions": ["Consult a doctor."]})

    # Voice Output
    speak(f"You may have {final_prediction}")

    return jsonify({
        "disease": final_prediction,
        "description": response["description"],
        "precautions": response["precautions"]
    })

if __name__ == "__main__":
    app.run(debug=True)
