import matplotlib.pyplot as plt
import numpy as np

X = np.array([1, 2, 3, 4, 5])
Y = np.array([1, 2, 1.3, 3.75, 2.25])

plt.scatter(X, Y, color='red')
plt.xlabel("Area (1000 sq. ft.)")
plt.ylabel("Price (lakhs)")
plt.title("Area vs Price")
plt.grid(True)
plt.show()
