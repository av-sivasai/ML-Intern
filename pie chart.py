import matplotlib.pyplot as plt

labels = ['Apple', 'Banana', 'Grapes', 'Orange']
sizes = [30, 25, 25, 20]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140,explode=(0, 0.1, 0, 0))  # Explode the second slice (Banana)
plt.title("Pie Chart")
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
#plt.explode([0, 0.1, 0, 0])  # Explode the second slice (Banana)