import numpy as np
import matplotlib.pyplot as plt

# Data
X = np.array([1, 2, 3, 4, 5])
Y = np.array([1, 2, 1.3, 3.75, 2.25])

# Define prediction function y = mx + c
def predict(x, m, c):
    return m * x + c

# Initial guess
m = 0.5
c = 0.5
y_pred = predict(X, m, c)

# Plot original data and prediction line
plt.scatter(X, Y, color='red', label='Actual Data')
plt.plot(X, y_pred, color='blue', label='Prediction Line')
plt.xlabel("Area")
plt.ylabel("Price")
plt.title("Initial Prediction Line")
plt.legend()
plt.grid(True)
plt.show()
