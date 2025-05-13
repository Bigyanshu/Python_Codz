# Ravel & Fatten are converts multidimensional array into single array

import numpy as np

# IF u take float in array then it will convert into float
x = np.array([[[1.2, 2.4, 4.5],[11,22,44],[1,2,4]]])
# rf = x.ravel()
# print("Ravel & Fatten is : ",rf)
print(x.ravel())
print(x.dtype)

str = np.array([[[11,22,66,77,],[1,3,7,9],[111,333,444,555]]])
# rf = str.flatten()
# print("Fatten & Ravel is : ",rf)
print(str.flatten())
print(str.dtype)