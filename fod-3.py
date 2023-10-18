import numpy as np
import pandas as pd

# Assuming you have a CSV file named "housing.csv" with a column "price" and "Bedrooms" in it
# Load the CSV file into a Pandas DataFrame
data = pd.read_csv("housing.csv")

# Extract the "price" column as a NumPy array
price = np.array(data["price"])

# Filter rows with more than 4 bedrooms
more_than_4 = data[data["Bedrooms"] > 4]

# Calculate the average price for the filtered rows
avg_price = np.mean(more_than_4["price"])
print("Average Sales price is", avg_price)
