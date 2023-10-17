#program-1
import numpy as np


student_scores = np.array([
    [9, 8, 9, 7],
    [9, 9, 8, 7],
    [9, 8, 9, 7],
    [9, 9, 8, 7],
    [9, 8, 9, 7],
    [9, 9, 8, 7],
    [9, 8, 9, 7],
    [9, 9, 8, 7],
    [9, 8, 9, 7],
    [9, 9, 8, 7],
    [9, 8, 9, 7],
    [9, 9, 8, 7],
    [9, 8, 9, 7],
    [9, 9, 8, 7],
    [9, 8, 9, 7],
    [9, 9, 8, 7],
    [9, 8, 9, 7],
    [9, 9, 8, 7],
    [9, 8, 9, 7],
    [9, 9, 8, 7],
    [9, 8, 9, 7],
    [9, 9, 8, 7],
    [9, 8, 9, 7],
    [9, 9, 8, 7],
    [9, 8, 9, 7],
    [9, 9, 8, 7],
    [9, 8, 9, 7],
    [9, 9, 8, 7],
    [9, 8, 9, 7],
    [9, 9, 8, 7],
    [9, 8, 9, 7],
])

subject_averages = np.mean(student_scores, axis=0)
highest_avg_subject = np.argmax(subject_averages)

print("Average Scores for Each Subject:")
for subject, avg_score in zip(["Math", "Science", "English", "History"], subject_averages):
    print(f"{subject}: {avg_score:.2f}")

print(f"The subject with the highest average score is: {['Math', 'Science', 'English', 'History'][highest_avg_subject]}")
