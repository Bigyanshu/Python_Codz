# 1_D Array Slicing

import numpy as np

a = np.array([1, 3, 5, 7, 9])
print("One D : ",a[0:])
print("One D : ",a[::2])
print("One D : ",a[::-1])
print()

# 2_D Array Slicing

t = np.array([[1, 3, 5, 7, 9], [2, 4, 6, 8, 0]])
print("Two D : ",t[0,0:4])
print("Two D : ",t[0,0::2])
print("Two D : ",t[1,::-1])