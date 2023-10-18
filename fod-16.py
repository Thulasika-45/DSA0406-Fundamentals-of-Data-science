import numpy as np
import scipy.stats as stats

# Sample conversion rate data for website design A and B (replace with your actual data)
conversion_rate_A = [0.1, 0.12, 0.11, 0.09, 0.14, 0.1, 0.11, 0.12, 0.09, 0.13, 0.1, 0.12]
conversion_rate_B = [0.08, 0.11, 0.1, 0.08, 0.12, 0.09, 0.1, 0.11, 0.08, 0.12, 0.08, 0.11]

# Perform a two-sample t-test
t_stat, p_value = stats.ttest_ind(conversion_rate_A, conversion_rate_B)

# Set the significance level (alpha)
alpha = 0.05  # You can adjust this based on your desired level of confidence

# Compare p-value to alpha
if p_value < alpha:
    print("There is a statistically significant difference in mean conversion rates between website design A and B.")
else:
    print("There is no statistically significant difference in mean conversion rates between website design A and B.")
