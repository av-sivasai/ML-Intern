import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(10000)
# bool1=data > -1
# bool2=data < 1
# bool=bool1 & bool2
# data = data[bool]
# print("Data points within range (-1, 1):", len(data))
plt.hist(data,bins=100, color='purple', edgecolor='black')
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()
