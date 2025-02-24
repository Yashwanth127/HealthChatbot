Disease Prediction System

📌 Project Description

The Disease Prediction System is an AI-based web application that predicts diseases based on user-provided symptoms. It uses a trained machine learning model to analyze symptoms and provide the correct disease name along with recommended precautions. The system also features an interactive chatbot animation for an engaging user experience.

🚀 Features

AI-powered Disease Prediction: Predicts diseases based on symptoms.

Correct Precautions: Provides verified medical advice.

Chatbot Animation: Enhances user experience.

Voice Output (Optional): Reads out the predictions.

Mute/Unmute Feature: User can enable or disable voice assistance.

📂 Project Structure

├── app.py                 # Backend Flask API
├── train_model.py         # AI Model Training Script
├── disease_model.pkl      # Trained Machine Learning Model
├── templates/
│   ├── index.html        # Frontend UI
│   ├── style.css         # Styles for UI & chatbot animation
├── static/
│   ├── chatbot.gif       # Chatbot animation asset
├── disease_symptoms_precautions.csv  # Dataset
├── README.md             # Project Documentation

🔧 Installation & Setup

1️⃣ Install Dependencies

Make sure Python is installed, then install required packages:

pip install flask pandas scikit-learn joblib

2️⃣ Train the Model

Run the following command to train the AI model:

python train_model.py

This will generate disease_model.pkl.

3️⃣ Run the Flask Server

Start the backend API:

python app.py

The server will run at http://127.0.0.1:5000/.

4️⃣ Open the Web Application

Open http://127.0.0.1:5000/ in a web browser.

Enter symptoms (comma-separated).

Click Predict to get the disease name and precautions.

📜 API Endpoints

Method

Endpoint

Description

POST

/predict

Takes symptoms as input and returns disease prediction with precautions

🎯 Future Improvements

🏥 Integration with medical databases for real-time disease updates.

🗣️ Voice-controlled chatbot for interactive symptom analysis.

📊 Historical Data Storage for personalized medical suggestions.

📌 Author

Developed by [Yashwanth Kumar S] 🚀

