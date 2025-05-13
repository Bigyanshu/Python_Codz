import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 3, 5, 4])  # Positions for bars on the y-axis
y = np.array([7, 9, 3, 6])  # Lengths of bars

c = 'g'  # Color for the bars
plt.title("Horizontal Bar Graph",color="grey")
# Create horizontal bars with specified color and height
plt.barh(x, y, color=c, height=0.2)
plt.xlabel('X-axis--->',color='b')
plt.ylabel('Y-axis--->',color='b')
plt.legend()
plt.show()