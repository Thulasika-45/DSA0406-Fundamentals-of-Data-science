import numpy as np
import pandas as pd
import scipy.stats as stats

# Function to generate random data (you can replace this with your actual data)
def generate_random_data(sample_size):
    # Simulate rare element concentration data
    data = np.random.normal(loc=10, scale=2, size=sample_size)
    return data

# Function to calculate the required sample size for a given confidence level and precision
def calculate_sample_size(confidence_level, precision):
    z = stats.norm.ppf(1 - (1 - confidence_level) / 2)  # Z-value for the confidence level
    required_sample_size = (z**2) / (precision**2)
    return int(np.ceil(required_sample_size))

# User input for sample size, confidence level, and precision
sample_size = int(input("Enter the desired sample size: "))
confidence_level = float(input("Enter the confidence level (e.g., 0.95 for 95% confidence): "))
precision = float(input("Enter the desired level of precision: "))

# Generate random data for the specified sample size
data = generate_random_data(sample_size)

# Calculate the required sample size
required_sample_size = calculate_sample_size(confidence_level, precision)

# Check if the user-specified sample size is sufficient
if sample_size >= required_sample_size:
    print(f"The provided sample size ({sample_size}) is sufficient for the desired level of precision.")
else:
    print(f"The provided sample size ({sample_size}) may not be sufficient. Consider using a sample size of at least {required_sample_size}.")

# Calculate confidence interval for the population mean based on user input
mean = np.mean(data)
std_dev = np.std(data, ddof=1)  # ddof=1 for Bessel's correction
margin_of_error = stats.norm.ppf(1 - (1 - confidence_level) / 2) * (std_dev / np.sqrt(sample_size))
confidence_interval = (mean - margin_of_error, mean + margin_of_error)

# Create a DataFrame with the generated data
df = pd.DataFrame({'Concentration': data})

print("Sample Mean:", mean)
print(f"Confidence Interval (at {confidence_level*100}%): {confidence_interval}")
print("\nSample Data:")
print(df.head())
