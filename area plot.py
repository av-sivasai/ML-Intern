import matplotlib.pyplot as plt
import numpy as np

days = np.arange(1, 6)
sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]
labels = ['Sleeping', 'Eating', 'Working', 'Playing']
data = np.vstack([sleeping, eating, working, playing])

plt.stackplot(days, data, labels=labels)
plt.title("Area Plot")
plt.xlabel("Day")
plt.ylabel("Hours")
plt.legend(loc='upper left')
plt.show()
