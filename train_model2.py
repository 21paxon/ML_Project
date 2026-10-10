
from sklearn.linear_model import LinearRegression

# Training data
# X = hours studied
X = [[1], [2], [3], [4], [5],
     [6], [7], [8], [9], [10]]

# y = exam scores
y = [15, 22, 28, 40, 45,
     58, 65, 72, 88, 95]

# Create the model
model = LinearRegression()

# Train the model
model.fit(X, y)

# Make predictions
prediction = model.predict([[6]])
prediction2 = model.predict([[8]])

# Display results
print("Training examples:", len(X))
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)
print("Predicted score for 6 hours:", prediction[0])
print("Predicted score for 8 hours:", prediction2[0])
