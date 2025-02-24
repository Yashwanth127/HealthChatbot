import joblib
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
import os

# Create the 'models' directory if it doesn't exist
os.makedirs("models", exist_ok=True)

# Load dataset
data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)

# Train Decision Tree Model
dt_model = DecisionTreeClassifier()
dt_model.fit(X_train, y_train)

# Train SVM Model
svm_model = SVC(probability=True)
svm_model.fit(X_train, y_train)

# Save models in the 'models/' directory
joblib.dump(dt_model, "models/decision_tree.pkl")
joblib.dump(svm_model, "models/svm_model.pkl")

print("✅ Models saved successfully in the 'models' folder!")
