import pandas as pd
import numpy as np
import scipy.stats as stats

# Create a synthetic DataFrame with random customer ratings
data = {
    "product_category": ["Electronics"] * 200,  # Chosen product category
    "rating": np.random.randint(1, 6, size=200)  # Random ratings between 1 and 5
}
df = pd.DataFrame(data)

# Calculate the sample mean rating for the selected category
sample_mean_rating = df[df["product_category"] == "Electronics"]["rating"].mean()

# Determine the sample size (number of reviews)
sample_size = len(df[df["product_category"] == "Electronics"])

# Choose a confidence level (e.g., 95%) and determine the Z-value
confidence_level = 0.95  # You can adjust this
z_value = stats.norm.ppf(1 - (1 - confidence_level) / 2)

# Calculate the standard error of the mean (SEM)
sample_std_dev = df[df["product_category"] == "Electronics"]["rating"].std()
sem = sample_std_dev / np.sqrt(sample_size)

# Calculate the margin of error (MOE)
margin_of_error = sem * z_value

# Calculate the confidence interval for the population mean rating
confidence_interval = (sample_mean_rating - margin_of_error, sample_mean_rating + margin_of_error)

# Print the results
print(f"Sample Mean Rating for Electronics: {sample_mean_rating:.2f}")
print(f"Sample Size: {sample_size}")
print(f"Confidence Interval (at {confidence_level*100}%): {confidence_interval}")
