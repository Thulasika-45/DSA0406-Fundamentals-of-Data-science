import matplotlib.pyplot as plt

# Sample data (replace with your actual data)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
temperature = [10.2, 11.5, 14.1, 18.3, 22.0, 26.7, 29.4, 29.1, 25.5, 20.2, 15.0, 11.4]

# Create a line plot for monthly temperature
plt.plot(months, temperature, marker='o', linestyle='-', color='b', label='Monthly Temperature (°C)')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.title('Monthly Temperature Data')
plt.legend()
plt.grid(True)

# Show the plot (if you want to display it)
plt.show()
