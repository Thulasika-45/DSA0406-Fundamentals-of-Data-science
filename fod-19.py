from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import numpy as np

# Define your dataset (replace with actual data)
X = [[1.0, 2.0], [2.0, 3.0], [3.0, 4.0], [4.0, 5.0], [5.0, 6.0]]
y = [0, 1, 0, 1, 0]  # Example labels (0 for no condition, 1 for the condition)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# User input for the number of neighbors (k)
k = int(input("Enter the number of neighbors (k): "))

# Create the KNN classifier with the chosen value of k
knn = KNeighborsClassifier(n_neighbors=k)

# Fit the classifier to the training data
knn.fit(X_train, y_train)

# Prompt the user to input features for a new patient
new_patient_features = np.array([float(x) for x in input("Enter the patient's symptom features separated by spaces: ").split()])

# Use the KNN classifier to predict the condition for the new patient
prediction = knn.predict([new_patient_features])

if prediction[0] == 0:
    print("The patient is predicted to have no medical condition.")
else:
    print("The patient is predicted to have the medical condition.")
