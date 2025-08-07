import numpy as np
import matplotlib.pyplot as plt

# Data
X = np.array([1, 2, 3, 4, 5])
Y = np.array([1, 2, 1.3, 3.75, 2.25])

# Initialize parameters
m = 0.0
c = 0.0
lr = 0.01
epochs = 1000
n = len(X)

# Gradient Descent
for _ in range(epochs):
    Y_pred = m * X + c
    error = Y - Y_pred
    dm = (-2/n) * np.sum(X * error)
    dc = (-2/n) * np.sum(error)
    m = m - lr * dm
    c = c - lr * dc

print(f"Trained m: {m:.2f}, Trained c: {c:.2f}")

# Final plot
plt.scatter(X, Y, color='red', label="Actual Data")
plt.plot(X, m * X + c, color='green', label="Trained Line")
plt.xlabel("Area")
plt.ylabel("Price")
plt.title("Trained Linear Regression Model")
plt.legend()
plt.grid(True)
plt.show()

