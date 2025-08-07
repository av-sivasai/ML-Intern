import numpy as np
import matplotlib.pyplot as plt

# Sample data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10]) 

# Initialize parameters
theta0 = 0
theta1 = 0
alpha = 0.01
epochs = 1000
m = len(x)

# Gradient descent loop
for _ in range(epochs):
    h = theta0 + theta1 * x
    error = h - y
    grad0 = (1/m) * np.sum(error)
    grad1 = (1/m) * np.sum(error * x)
    theta0 -= alpha * grad0
    theta1 -= alpha * grad1

print(f"Final theta0: {theta0:.4f}, theta1: {theta1:.4f}")

# Plot result
plt.scatter(x, y, label='Data')
plt.plot(x, theta0 + theta1 * x, color='red', label='Prediction')
plt.legend()
plt.show()