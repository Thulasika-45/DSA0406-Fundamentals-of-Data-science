import matplotlib.pyplot as plt

# Sample data (replace with your actual data)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
rainfall = [30.2, 27.5, 35.1, 50.3, 75.0, 90.7, 110.4, 105.1, 85.5, 65.2, 45.0, 38.4]

# Create a scatter plot for monthly rainfall
plt.scatter(months, rainfall, color='g', label='Monthly Rainfall (mm)')
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')
plt.title('Monthly Rainfall Data')
plt.legend()

# Show the plot (if you want to display it)
plt.show()
