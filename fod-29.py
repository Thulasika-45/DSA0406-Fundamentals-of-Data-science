import pandas as pd
import numpy as np

# Load stock data from a CSV file (replace 'stock_data.csv' with your file)
data = pd.read_csv('stock_data.csv')

# Ensure the CSV file has a 'Date' column with date values and a 'Close' column with closing prices

# Calculate daily returns
data['Daily_Return'] = data['Close'].pct_change()

# Calculate standard deviation as a measure of variability
std_deviation = data['Daily_Return'].std()

# Calculate the average daily return
average_return = data['Daily_Return'].mean()

# Calculate the maximum and minimum daily returns
max_return = data['Daily_Return'].max()
min_return = data['Daily_Return'].min()

# Determine the trading day with the maximum positive return and the maximum negative return
max_positive_return_day = data.loc[data['Daily_Return'].idxmax()]['Date']
max_negative_return_day = data.loc[data['Daily_Return'].idxmin()]['Date']

# Print insights and results
print(f"Standard Deviation (Variability): {std_deviation:.4f}")
print(f"Average Daily Return: {average_return:.4f}")
print(f"Maximum Daily Return: {max_return:.4f} on {max_positive_return_day}")
print(f"Minimum Daily Return: {min_return:.4f} on {max_negative_return_day}")

# Additional analysis and visualization can be added as needed.
