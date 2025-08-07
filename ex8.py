import numpy as np
import matplotlib.pyplot as plt

# ---------- Function Definitions ---------- #

def feature_normalize(X):
    """ Normalize features (mean = 0, std = 1) """
    mu = np.mean(X, axis=0)
    sigma = np.std(X, axis=0)
    X_norm = (X - mu) / sigma
    return X_norm, mu, sigma

def compute_cost(X, y, theta):
    """ Mean Squared Error cost function """
    m = len(y)
    predictions = X @ theta
    error = predictions - y
    return (1/(2*m)) * np.sum(error**2)

def gradient_descent(X, y, theta, alpha, epochs):
    """ Performs gradient descent to learn theta """
    m = len(y)
    cost_history = []

    for _ in range(epochs):
        error = (X @ theta) - y
        gradient = (1/m) * (X.T @ error)
        theta -= alpha * gradient
        cost = compute_cost(X, y, theta)
        cost_history.append(cost)

    return theta, cost_history

def predict(X, mu, sigma, theta):
    """ Make predictions on new data after normalization """
    X_norm = (X - mu) / sigma
    X_padded = np.c_[np.ones((X.shape[0], 1)), X_norm]
    return X_padded @ theta

# ---------- Dataset ---------- #
# Let's say we are predicting car price from features:
# [engine size, horsepower, age]
X = np.array([
    [1500, 100, 5],
    [1800, 120, 3],
    [2000, 140, 2],
    [2200, 160, 1],
    [2500, 180, 1]
])
y = np.array([7.5, 9.0, 10.5, 12.0, 13.5])  # price in lakhs

# ---------- Preprocessing ---------- #
X_norm, mu, sigma = feature_normalize(X)
X_b = np.c_[np.ones((X.shape[0], 1)), X_norm]  # Add bias

# ---------- Initialize Parameters ---------- #
theta = np.zeros(X_b.shape[1])
alpha = 0.01
epochs = 500

# ---------- Train Model ---------- #
theta_final, cost_history = gradient_descent(X_b, y, theta, alpha, epochs)

# ---------- Results ---------- #
print("Final Theta Values:", theta_final)
print("Final Cost:", cost_history[-1])

# ---------- Plot Cost ---------- #
plt.plot(range(epochs), cost_history)
plt.xlabel("Epochs")
plt.ylabel("Cost")
plt.title("Cost Function over Time")
plt.grid(True)
plt.show()

# ---------- Predict ---------- #
new_car = np.array([[2100, 150, 2]])
predicted_price = predict(new_car, mu, sigma, theta_final)
print(f"Predicted price for new car: {predicted_price[0]:.2f} lakhs")
