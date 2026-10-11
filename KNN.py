from sklearn.neighbors import KNeighborsClassifier

X = [[1], [2], [3], [6], [7], [8]]
y = [0, 0, 0, 1, 1, 1]

model = KNeighborsClassifier(n_neighbors=3)

model.fit(X, y)

prediction = model.predict([[6.5]])

print("Prediction:", prediction[0])