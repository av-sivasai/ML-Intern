import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x, y1, label='Sine Wave', color='blue')
plt.plot(x, y2, label='Cosine Wave', color='orange')
plt.title("Line Plot")
plt.xlabel("x-values")
plt.ylabel("sin(x)")
plt.legend()
plt.grid(True)
plt.show()