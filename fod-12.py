import pandas as pd

data = {
    'CustomerID': [1, 2, 3, 4, 5],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [35, 28, 42, 28, 53],
    'PurchaseDate': ['2023-09-05', '2023-09-15', '2023-08-20', '2023-09-10', '2023-09-25']
}

sales_data = pd.DataFrame(data)

start_date = '2023-09-01'
end_date = '2023-09-30'

sales_data['PurchaseDate'] = pd.to_datetime(sales_data['PurchaseDate'])

sales_data_last_month = sales_data[(sales_data['PurchaseDate'] >= start_date) & (sales_data['PurchaseDate'] <= end_date)]

age_distribution = sales_data_last_month['Age'].value_counts().sort_index()

print("Age Frequency Distribution for the Past Month:\n", age_distribution)
