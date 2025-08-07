import numpy as np

# Sample data: 3 examples, 2 features (x1, x2)
X = np.array([
    [1, 2],
    [2, 3],
    [3, 4]
])
y = np.array([5, 8, 11])  # Target values

# Add bias term (x0 = 1)
X_b = np.c_[np.ones((X.shape[0], 1)), X]  # shape: (3, 3)

# Initialize theta
theta = np.zeros(X_b.shape[1])
alpha = 0.01
epochs = 1000
m = len(y)

# Gradient descent loop
for _ in range(epochs):
    h = X_b @ theta
    error = h - y
    grad = (1/m) * X_b.T @ error
    theta -= alpha * grad

print(f"Final theta values: {theta}")