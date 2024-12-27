myLst = [1, 3, 5, 7, 9]

squaredList = []
for item in myLst:
    # squaredList.append(item * item)
    squaredList.append(item ** 2)
    # squaredList.append(item + item)
    # squaredList.append(item - item)
    # squaredList.append(item / item)
    # squaredList.append(item % item)
print("squaredList is : ",squaredList) 

# Efficient Way
myLst = [1, 3, 5, 7, 9]
squaredList = [item * item for item in myLst]
print("squaredList is : ",squaredList) 
