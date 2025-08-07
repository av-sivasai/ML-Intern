import matplotlib.pyplot as plt
import numpy as np

data = [np.random.normal(0, std, 100) for std in range(1, 4)]

plt.boxplot(data, vert=True, patch_artist=True)
plt.title("Box Plot")
plt.xlabel("Dataset")
plt.ylabel("Value")
plt.xticks([1, 2, 3], ['Std=1', 'Std=2', 'Std=3'])
plt.grid(True)
plt.show()
