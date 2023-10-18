import pandas as pd

# Sample data (replace with your actual dataset)
data = {
    'post_id': [1, 2, 3, 4, 5, 6, 7, 8],
    'likes': [10, 20, 15, 30, 25, 20, 40, 10]
}

# Create a DataFrame from the sample data
df = pd.DataFrame(data)

# Calculate the frequency distribution of likes
likes_distribution = df['likes'].value_counts().reset_index()
likes_distribution.columns = ['Likes', 'Frequency']

# Sort the distribution by the number of likes (optional)
likes_distribution = likes_distribution.sort_values(by='Likes')

# Display the frequency distribution
print("Frequency Distribution of Likes:")
print(likes_distribution)
