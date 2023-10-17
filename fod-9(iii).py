
import matplotlib.pyplot as plt

# Sample data (you would use your own dataset)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [10000, 12000, 14000, 11000, 13000, 15000]

# Create a bar plot to visualize monthly sales
plt.bar(months, sales, color='g', label='Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales Amount')
plt.title('Monthly Sales Data')
plt.legend()
# Show the plot (if you want to display it)
plt.show()
