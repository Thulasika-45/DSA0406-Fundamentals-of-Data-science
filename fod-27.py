import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load your dataset (replace 'your_dataset.csv' with your dataset file)
data = pd.read_csv('your_dataset.csv')

# Bivariate analysis: Select the feature (e.g., 'house_size')
feature = 'house_size'
target = 'house_price'

# Visualize the relationship between the feature and target
plt.scatter(data[feature], data[target])
plt.xlabel(feature)
plt.ylabel(target)
plt.title(f'Bivariate Analysis: {feature} vs. {target}')
plt.show()

# Data preprocessing
X = data[[feature]]
y = data[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Model evaluation
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse:.2f}')
print(f'R-squared (R2) Score: {r2:.2f}')

# Visualize the model's predictions
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.scatter(X_test, y_pred, color='red', label='Predicted')
plt.xlabel(feature)
plt.ylabel(target)
plt.legend()
plt.title('Model Predictions vs. Actual')
plt.show()

# Interpret the model (coefficients)
print(f'Coefficient: {model.coef_[0]:.2f}')
print(f'Intercept: {model.intercept_:.2f}')

# Make predictions for new data points
new_data = pd.DataFrame({feature: [100, 150, 200]})
predicted_prices = model.predict(new_data)
print('Predicted prices for new data:')
print(predicted_prices)
