import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load your car dataset (replace 'your_car_dataset.csv' with your dataset file)
data = pd.read_csv('your_car_dataset.csv')

# Select a set of features
selected_features = ['engine_size', 'horsepower', 'fuel_efficiency', 'curb_weight']

# Create the feature matrix (X) and the target variable (y)
X = data[selected_features]
y = data['price']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Model evaluation
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse:.2f}')
print(f'R-squared (R2) Score: {r2:.2f}')

# Get coefficients (importance) of each feature
coefficients = pd.Series(model.coef_, index=selected_features)
coefficients = coefficients.sort_values(ascending=False)

print('Feature Importance (Coefficients):')
print(coefficients)

# Visualize the model's predictions
plt.scatter(y_test, y_pred)
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.title('Actual Prices vs. Predicted Prices')
plt.show()

# Interpret the model
intercept = model.intercept_
print(f'Intercept (Price when all features are 0): {intercept:.2f}')

# Provide insights to the marketing team
print('Influential factors affecting car prices:')
print(f"The most influential factor: {coefficients.index[0]}")
