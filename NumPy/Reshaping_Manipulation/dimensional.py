import numpy as np

# One Dimensional Array
one = np.array([1,2,3,4])
print("One Dim : ",one, one.ndim)

# Two Dimensional Array
two = np.array([[1,3,5] , [3,89,97]])
print("Two Dim : ",two, two.ndim)

# Three Dimensional Array

# Type_1
# three = np.array([[[3.1, 3.2, 4], [3.9, 3.6, 3], [[7,9,97] , [3,5,7]] ]])
# print("Three Dim : ",three, three.ndim)

# Type-2
thr = np.array([3,3.5,3.7], ndmin=3)
print("Three Dim : ",thr, thr.ndim)

# Five Dimensional Array

# Type-1
five = np.array([5.1 , 5.3, 5.5], ndmin= 5)
print("Five Dim : ",five, five.ndim)

# Type-2
fivE = np.array([[[[[5,7,9,0]]]]])
print("Five Dim : ",fivE, fivE.ndim)