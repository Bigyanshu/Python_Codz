# Data Types in Numpy
'''
i - integer     u - unsigned integer    b - boolean     f - float   c - complex float       m - timedelta
M - datetime     U - unicode string     O - object      S - string    V - void (fixed chunk of memory for other type(void))
'''

import numpy as np

z = np.array(['Animal', 'Mahy', 'Mahi'])
print("Data Type is : ",z.dtype)    # Unicode String - <U6

k = np.array([1,3,5,7,9], dtype = "S")
print("With Type is : ",k)  # With Type is :  [b'1' b'3' b'5' b'7' b'9'] - "b" rep. string type
print(f"Data Type is :  {k.dtype}") #Both give same output -|S1
print("Data Type is : ", k.dtype)   #Both give same output -|S1


# Create an array with data type 4 bytes integer

l = np.array([1.0,4,6.4,7,4.4], dtype='i4')
print(l, l.dtype)

l = np.array([1.0,4,6.4,7,4.4], dtype='i8')
print(l, l.dtype)