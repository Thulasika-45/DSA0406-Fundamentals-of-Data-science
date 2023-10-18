from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Create a Decision Tree classifier and fit it to the dataset
clf = DecisionTreeClassifier(random_state=0)
clf.fit(X, y)

# Prompt the user to input new flower data
sepal_length = float(input("Enter sepal length: "))
sepal_width = float(input("Enter sepal width: "))
petal_length = float(input("Enter petal length: "))
petal_width = float(input("Enter petal width: "))

# Use the classifier to predict the species of the new flower
new_flower = [[sepal_length, sepal_width, petal_length, petal_width]]
prediction = clf.predict(new_flower)

# Display the predicted species to the user
species = iris.target_names[prediction[0]]
print(f"The predicted species of the new flower is: {species}")
