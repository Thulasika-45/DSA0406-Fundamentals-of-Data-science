import matplotlib.pyplot as plt

# Sample data (you would use your own dataset)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [10000, 12000, 14000, 11000, 13000, 15000]

# Create a line plot to predict sales over time
plt.plot(months, sales, marker='o', linestyle='-', color='b', label='Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales Amount')
plt.title('Predicted Monthly Sales')
plt.legend()
plt.grid(True)

# Show the plot (if you want to display it)
plt.show()
