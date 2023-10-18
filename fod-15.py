import numpy as np
import scipy.stats as stats

# Hypothetical data (replace with actual data)
new_drug_data = [5, 4, 6, 3, 4, 7, 2, 5, 6, 4, 5, 6, 3, 4, 5, 6, 7, 4, 5, 3, 5, 4, 6, 7, 4, 5, 3, 4, 6, 5, 4, 7, 6, 4, 5, 3, 4, 5, 6, 7, 4, 5, 6, 3, 4, 5, 6, 7]
placebo_data = [6, 7, 5, 8, 7, 5, 9, 6, 7, 8, 6, 5, 7, 8, 6, 5, 4, 7, 6, 9, 6, 7, 5, 4, 8, 7, 9, 6, 5, 7, 8, 6, 5, 7, 8, 5, 6, 7, 8, 6, 5, 7, 8, 6, 7, 5, 8]

# Sample sizes
n1 = len(new_drug_data)
n2 = len(placebo_data)

# Sample means
x_bar1 = np.mean(new_drug_data)
x_bar2 = np.mean(placebo_data)

# Sample standard deviations
s1 = np.std(new_drug_data, ddof=1)
s2 = np.std(placebo_data, ddof=1)

# Confidence level
confidence_level = 0.95

# Calculate the standard error
se1 = s1 / np.sqrt(n1)
se2 = s2 / np.sqrt(n2)

# Calculate the critical value for the confidence interval
z = stats.norm.ppf(1 - (1 - confidence_level) / 2)

# Calculate the margin of error
margin_of_error1 = z * se1
margin_of_error2 = z * se2

# Calculate the confidence intervals
confidence_interval1 = (x_bar1 - margin_of_error1, x_bar1 + margin_of_error1)
confidence_interval2 = (x_bar2 - margin_of_error2, x_bar2 + margin_of_error2)

# Print the confidence intervals
print("95% Confidence Interval for New Drug Group:", confidence_interval1)
print("95% Confidence Interval for Placebo Group:", confidence_interval2)
