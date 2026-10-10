
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# All our data
X = [[1], [2], [3], [4], [5],
     [6], [7], [8], [9], [10]]

y = [15, 22, 28, 40, 45,
     58, 65, 72, 88, 95]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create the model
model = LinearRegression()

# Train using training data only
model.fit(X_train, y_train)

# Predict scores for testing data
predictions = model.predict(X_test)

# Compare predictions with actual scores
print("Training examples:", len(X_train))
print("Testing examples:", len(X_test))
print("Actual scores:", y_test)
print("Predicted scores:", predictions)
print("Mean Absolute Error:",
      mean_absolute_error(y_test, predictions))
