from sklearn.cluster import KMeans
import numpy as np

# Define your dataset (replace with actual data)
X = np.array([
    [10, 5, 3],
    [15, 3, 2],
    [7, 7, 1],
    [2, 12, 4],
    [5, 15, 3],
    [12, 6, 2]
])

# Create a K-Means model and fit it to the dataset (you can adjust the number of clusters)
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(X)

# Prompt the user to input shopping-related features for a new customer
new_customer_features = np.array([float(x) for x in input("Enter shopping-related features separated by spaces: ").split()])

# Use the K-Means model to assign the new customer to one of the existing segments
segment = kmeans.predict([new_customer_features])

print(f"The new customer is assigned to segment {segment[0]}.")
