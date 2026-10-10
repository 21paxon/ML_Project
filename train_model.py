
# STEP 1: Import the algorithm
from sklearn.linear_model import LinearRegression

# STEP 2: Prepare the training data
X = [[1], [2], [3], [4], [5], [6]]
y = [10, 20, 30, 40, 50, 60]

# STEP 3: Create the model
model = LinearRegression()

# STEP 4: Train the model
model.fit(X, y)

# STEP 5: Make a prediction
prediction = model.predict([[7]])

# STEP 6: Display the result
print("Predicted exam score:", prediction[0])
