import pandas as pd

# Assuming you already have the property_data DataFrame loaded

property_data = {
    'property_id': [1, 2, 3, 4, 5],
    'location': ['Location1', 'Location2', 'Location1', 'Location2', 'Location3'],
    'number_of_bedrooms': [3, 4, 3, 5, 2],
    'area_in_square_feet': [1500, 2000, 1800, 2200, 1200],
    'listing_price': [250000, 320000, 280000, 350000, 200000]
}
property_data= pd.DataFrame(property_data)
# 1. The average listing price of properties in each location
average_price_by_location = property_data.groupby('location')['listing_price'].mean()

# 2. The number of properties with more than four bedrooms
properties_more_than_4_bedrooms = len(property_data[property_data['number_of_bedrooms'] > 4])

# 3. The property with the largest area
property_with_largest_area = property_data[property_data['area_in_square_feet'] == property_data['area_in_square_feet'].max()]

# Display the results
print("Average Listing Price by Location:")
print(average_price_by_location)

print("\nNumber of Properties with More than Four Bedrooms:", properties_more_than_4_bedrooms)

print("\nProperty with the Largest Area:")
print(property_with_largest_area)
