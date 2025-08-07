import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 10)
y = np.cos(x)

plt.stem(x, y, basefmt=" ")  # Removed 'use_line_collection'
plt.title("Stem Plot")
plt.xlabel("x")
plt.ylabel("cos(x)")
plt.grid(True)
plt.show()
