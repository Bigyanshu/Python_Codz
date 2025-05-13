fruits = []

print(fruits)

f1 = input("Enter ur fruits :")
fruits.append(f1)
f2 = input("Enter ur fruits :")
fruits.append(f2)

fruits.append("papaya")

f3 = input("Enter Fruits Name:")
fruits.append(f3)

fruits.insert(0,"spike")
fruits.insert(3,"Hole")

f4 = input("Enter Fruits Name:")
fruits.append(f4)
f5 = input("Enter Fruits Name:")
fruits.append(f5)
# fruits.append(f5 = input("Enter Fruits Name:")) # Returns type error :list.append() takes no keyword arguments
f6 = input("Enter Fruits Name:")
fruits.append(f6)
f7 = input("Enter Fruits Name:")
fruits.append(f7)

print("Fruits List:", fruits)   

# input a list then append others fruits & add insert one fruits in original fruits