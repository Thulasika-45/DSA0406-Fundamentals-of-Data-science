import pandas as pd

# Assuming you have the order data in a DataFrame named order_data
data={"Customer ID":[1,2,3],
      "Product Name":["chocolate","note","pencil"],
      "Order Quantity":[3,2,1],
      "Order Date":["12-2-23","22-4-22","10-9-20"]}
# Create the DataFrame
order_data = pd.DataFrame(data)


# 1. Total number of orders made by each customer
customer_order_counts = order_data['Customer ID'].value_counts()

# 2. Average order quantity for each product
average_order_quantity_per_product = order_data.groupby('Product Name')['Order Quantity'].mean()

# 3. Earliest and latest order dates
earliest_order_date = order_data['Order Date'].min()
latest_order_date = order_data['Order Date'].max()

print("Total number of orders made by each customer:\n", customer_order_counts)
print("\nAverage order quantity for each product:\n", average_order_quantity_per_product)
print("\nEarliest order date:", earliest_order_date)
print("Latest order date:", latest_order_date)
