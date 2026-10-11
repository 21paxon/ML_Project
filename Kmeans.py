from sklearn.cluster import KMeans

# Customer data: monthly spending in thousands of RWF
X = [[20], [25], [30],
     [280], [300], [320]]

# Create a model that discovers 2 groups
model = KMeans(n_clusters=2, random_state=42, n_init=10)

# Learn the groups
model.fit(X)

# Display the group assigned to each customer
print(model.labels_)