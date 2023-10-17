import numpy as np

# Sample sales data for each quarter (replace this with your actual data)
sales_data = np.array([50000, 60000, 70000, 80000])

# Calculate the total sales for the year using np.sum
total_sales_year = np.sum(sales_data)

# Calculate the percentage increase from the first quarter to the fourth quarter
percentage_increase = ((sales_data[3] - sales_data[0]) / sales_data[0]) * 100

print("Total sales for the year:", total_sales_year)
print("Percentage increase from Q1 to Q4:", percentage_increase, "%")
