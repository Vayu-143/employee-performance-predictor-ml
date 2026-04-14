import os
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split

from src.data_generator import generate_data
from src.preprocessing import preprocess_data
from src.model import train_model
from src.evaluate import evaluate_model
from src.visualize import plot_performance_distribution, plot_confusion_matrix

os.makedirs("data", exist_ok=True)
os.makedirs("models", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

print("STEP 1: Generating Data...")
data = generate_data(500)

data.to_csv("data/employee_data.csv", index=False)

print("\nDataset Preview:\n", data.head())

print("STEP 2: Preprocessing...")
X, y = preprocess_data(data)

print("STEP 3: Splitting...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print("STEP 4: Training Model...")
model = train_model(X_train, y_train)

joblib.dump(model, "models/performance_model.pkl")

print("STEP 5: Evaluating...")
accuracy, cm, report, y_pred = evaluate_model(model, X_test, y_test)

print("\nAccuracy:", accuracy)
print("\nConfusion Matrix:\n", cm)
print("\nClassification Report:\n", report)

print("STEP 6: Visualization...")
plot_performance_distribution(data)
plot_confusion_matrix(cm)

# Feature Importance
import matplotlib.pyplot as plt

importances = model.feature_importances_
features = X.columns

plt.barh(features, importances)
plt.title("Feature Importance")
plt.savefig("outputs/feature_importance.png")
plt.show()

print("✅ PROJECT COMPLETED")