import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Load and preprocess customer data
data = pd.read_csv('customer_data.csv')
# Preprocess and scale data as needed

# Choose the number of clusters (e.g., 4)
num_clusters = 4

# Create and fit the K-Means model
kmeans = KMeans(n_clusters=num_clusters, random_state=0)
kmeans.fit(data)

# Add cluster labels to the original dataset
data['cluster'] = kmeans.labels_

# Analyze and interpret the results
for cluster in range(num_clusters):
    print(f"Cluster {cluster}:")
    print(data[data['cluster'] == cluster].describe())

# Use the segments for marketing
# Tailor marketing strategies for each cluster

# Visualization (for 2D data)
plt.scatter(data['feature1'], data['feature2'], c=data['cluster'])
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()
