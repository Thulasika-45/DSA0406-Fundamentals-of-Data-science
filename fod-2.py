import numpy as np
sales_data = np.array([
    [10.5, 15.2, 8.7],
    [7.3, 12.8, 9.4],
    [14.6, 10.9, 11.2]
])
average_price = np.mean(sales_data)
print(f"The average price of all products sold in the past month is: ${average_price:.2f}")
