import numpy as np

# Data
Y_true = np.array([1, 2, 1.3, 3.75, 2.25])
Y_pred = np.array([1, 1.5, 2, 2.5, 3])  # example predictions

def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

error = mean_squared_error(Y_true, Y_pred)
print("Mean Squared Error:", error)
