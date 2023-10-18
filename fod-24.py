from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import numpy as np

# Load your dataset and trained model (replace with your data and model)
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # Features
y_true = np.array([0, 1, 0])  # True labels
y_pred = np.array([0, 0, 1])  # Predicted labels

# Prompt the user to input the names of the features and target variable for evaluation
feature_names = input("Enter the names of the features separated by spaces: ").split()
target_variable = input("Enter the name of the target variable: ")

# Calculate evaluation metrics
accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)

# Display the evaluation metrics
print(f"Evaluation Metrics for {target_variable}:")
print(f"Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1-Score: {f1:.4f}")
