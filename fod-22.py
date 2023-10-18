from sklearn.linear_model import LogisticRegression
import numpy as np

# Define your dataset (replace with actual data)
X = np.array([[300, 12], [500, 24], [200, 6], [800, 36], [1000, 12]])  # Features
y = np.array([1, 0, 1, 0, 0])  # Churn status (1 for churned, 0 for not churned)

# Create a Logistic Regression model and fit it to the dataset
model = LogisticRegression()
model.fit(X, y)

# Prompt the user to input the features of a new customer
usage_minutes = int(input("Enter the usage minutes of the new customer: "))
contract_duration = int(input("Enter the contract duration of the new customer: "))

# Use the trained model to predict whether the new customer will churn
new_customer = np.array([[usage_minutes, contract_duration]])
prediction = model.predict(new_customer)

# Display the prediction to the user
if prediction[0] == 1:
    print("The new customer is predicted to churn.")
else:
    print("The new customer is predicted to not churn.")
