from sklearn.tree import DecisionTreeRegressor, export_text
import pandas as pd

# Load your car dataset (replace 'your_car_dataset.csv' with your dataset file)
data = pd.read_csv('your_car_dataset.csv')

# Get the features (excluding the target variable 'price') and target variable
feature_names = data.columns.tolist()
feature_names.remove('price')
target_variable = 'price'

# Create the CART regression model
cart_model = DecisionTreeRegressor(random_state=0)
cart_model.fit(data[feature_names], data[target_variable])

# Prompt the user to input the features of a new car
new_car_features = []
print("Enter the features of the new car:")
for feature in feature_names:
    value = input(f"{feature}: ")
    new_car_features.append(value)

# Convert the user input into a DataFrame
new_car_data = pd.DataFrame([new_car_features], columns=feature_names)

# Use the CART model to predict the price of the new car
predicted_price = cart_model.predict(new_car_data)

# Display the predicted price
print(f"The predicted price of the new car is: ${predicted_price[0]:.2f}")

# Display the decision path for the new car
decision_path = export_text(cart_model, feature_names=feature_names)
print("\nDecision Path:")
print(decision_path)
