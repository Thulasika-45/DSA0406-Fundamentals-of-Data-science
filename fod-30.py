import matplotlib.pyplot as plt
import numpy as np

# Sample data (replace with your actual data)
study_time = [2, 3, 1, 4, 5, 3, 6, 2, 4, 5]
exam_scores = [60, 70, 50, 80, 90, 75, 95, 65, 85, 90]

# Calculate the correlation coefficient
correlation = np.corrcoef(study_time, exam_scores)[0, 1]

# Create a scatter plot to visualize the relationship
plt.figure(figsize=(8, 6))
plt.scatter(study_time, exam_scores, color='blue', label=f'Correlation: {correlation:.2f}')
plt.xlabel("Study Time (hours)")
plt.ylabel("Exam Scores")
plt.title("Study Time vs. Exam Scores")
plt.legend()
plt.grid(True)

# Plot a trendline (regression line) to visualize the relationship
z = np.polyfit(study_time, exam_scores, 1)
p = np.poly1d(z)
plt.plot(study_time, p(study_time), "r--")

# Show the plot
plt.show()
