from sklearn.linear_model import LinearRegression
import numpy as np

# Define your dataset (replace with actual data)
X = np.array([[2500, 3], [3000, 4], [2000, 3], [3500, 4], [4000, 5]])  # Features: [area, number of bedrooms]
y = np.array([300000, 400000, 250000, 450000, 500000])  # Prices

# Create a Linear Regression model and fit it to the dataset
model = LinearRegression()
model.fit(X, y)

# Prompt the user to input the features of a new house
area = float(input("Enter the area of the new house: "))
bedrooms = int(input("Enter the number of bedrooms in the new house: "))

# Use the trained model to predict the price of the new house
new_house = np.array([[area, bedrooms]])
predicted_price = model.predict(new_house)

# Display the predicted price to the user
print(f"The predicted price of the new house is: ${predicted_price[0]:.2f}")
