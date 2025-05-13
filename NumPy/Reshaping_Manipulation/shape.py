import numpy as np

# 1_D Array Shape

one = np.array([1,2,3,4,5])  # (5,) - (5 elements inside 1 array)
print(one.shape)


# 2_D Array Shape

two = np.array([[1,3,5,7], [0,8,6,4]])  # (2, 4) - (2 array inside 4 element)
print(two.shape)

'''x_two = np.array([[1,3,5,7], [8,6,4]]) # Requested array has an inhomogeneous shape after 1 dimensions
print(x_two.shape)'''


# 3_D Array Shape

three = np.array([[[90,30,10],[11,22,33],[33,99,77]]])  # (1, 3, 3) - (1 array, 3 array, 3 element)
print(three.shape)