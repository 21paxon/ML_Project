
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# 1. Input: study hours
X = [[1], [2], [3], [4], [5],
     [6], [7], [8], [9], [10]]

# 2. Actual results: 0 = Fail, 1 = Pass
y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

# 3. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Create and train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# 5. Predict results for the test data
predictions = model.predict(X_test)

# 6. Evaluate the model
print("Accuracy:", accuracy_score(y_test, predictions))
print(classification_report(y_test, predictions, zero_division=0))

# 7. Predict for a student who studies 6 hours
result = model.predict([[6]])
print("Prediction for 6 study hours:", result[0])
