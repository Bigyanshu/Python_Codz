# Creating Zip Files

name = ["Apple", "Mac_Book", "Oranges"]
price = [180, 100000,90]

fruit = dict(zip(name,price))

print(fruit)

print(len(fruit))

# Using .get methid to retrieve data
print(fruit.get("Mac_Book"))
print(fruit.get("Apple"))

#Adding Fruits in existing Zip List
fruit["Kiwi"] = {"Premium": 200, "Branded": 150}
fruit["Banana"] = {"Small_Size_3inch": 10, "Large_Size_6inch":30, "Extra_Large_9inch": 70}

print(fruit)

print(fruit.get("Banana"))

# .update method to update existing Fruits in Zip List
fruit.update({"Apple":100})

# Deleting fruits by .pop method
fruit.pop("Apple")
fruit.pop("Oranges")
# fruit.pop("Small_Size_3inch") # sub fruits can't deleted
fruit.popitem()# If u delete fruits it delete items by your right to left
fruit.popitem()
fruit.popitem()

v = fruit
print()
print("Fruits are :",fruit)
if(fruit == v):
    print("Knull")