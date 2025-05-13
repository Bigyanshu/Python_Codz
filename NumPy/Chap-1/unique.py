import numpy as np

k = np.array([1,4,5,7,9,8,3,2,6,7,4,8,9,6,4,5,3])
u = np.unique(k, return_index =True, return_counts=True)
print("Unique Value is : ", u) # (array([1, 2, 3, 4, 5, 6, 7, 8, 9]), array([0, 7, 6, 1, 2, 8, 3, 5, 4]), array([1, 1, 2, 3, 2, 2, 2, 2, 2]))
#              '''  These are                "Elements"                           "Positions"                  No of "Duplicates"    '''

# Another way

k = np.array([11, 24, 45, 77, 99, 38, 43, 72, 86, 97, 43, 86, 99, 86, 24, 45, 43])
u, indices, duplicates = np.unique(k, return_index=True, return_counts = True)
print("Unique values are  : ", u)   # [11 24 38 43 45 72 77 86 97 99]
print("Indices of unique values:", indices) # [0 1 5 6 2 7 3 8 9 4]
print("NO of Duplicates : ", duplicates) # [1 2 1 3 2 1 1 3 1 2]
