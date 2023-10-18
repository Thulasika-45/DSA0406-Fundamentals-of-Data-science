import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

# Create a DataFrame with the given data
data = pd.DataFrame({
    'age': [23, 23, 27, 27, 39, 41, 47, 49, 50, 54, 54, 56, 57, 58, 58, 60, 61, 52],
    '%fat': [9.5, 26.5, 7.8, 17.8, 31.4, 25.9, 27.4, 27.2, 31.2, 34.6, 42.5, 28.8, 33.4, 30.2, 34.1, 32.9, 41.2, 35.7]
})

# Calculate mean, median, and standard deviation for age and %fat
age_mean = data['age'].mean()
age_median = data['age'].median()
age_std = data['age'].std()

fat_mean = data['%fat'].mean()
fat_median = data['%fat'].median()
fat_std = data['%fat'].std()

print("Age Mean:", age_mean)
print("Age Median:", age_median)
print("Age Standard Deviation:", age_std)
print("%fat Mean:", fat_mean)
print("%fat Median:", fat_median)
print("%fat Standard Deviation:", fat_std)

# Create boxplots for age and %fat
plt.figure(figsize=(10, 5))
data.boxplot(column=['age', '%fat'])
plt.title("Boxplots for Age and %fat")
plt.ylabel("Value")
plt.show()

# Create a scatter plot for age and %fat
plt.figure(figsize=(8, 6))
plt.scatter(data['age'], data['%fat'])
plt.title("Scatter Plot of Age vs. %fat")
plt.xlabel("Age")
plt.ylabel("%fat")
plt.grid(True)
plt.show()

# Create a Q-Q plot for age and %fat
plt.figure(figsize=(10, 5))
stats.probplot(data['age'], dist="norm", plot=plt)
plt.title("Q-Q Plot for Age")
plt.show()

plt.figure(figsize=(10, 5))
stats.probplot(data['%fat'], dist="norm", plot=plt)
plt.title("Q-Q Plot for %fat")
plt.show()
