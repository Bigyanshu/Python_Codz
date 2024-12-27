# Enumerate or Efficiently

lsts = [ 1, 11, 111, 1111, 11111]

for index,item in enumerate(lsts):
    print(f"The Index is {index} & it's item is {item}")

print()

# Normal List indexing

lst = [3,79,793,1000]

index = 0 
for item in lst:
    print(f"The index {index} & it's item {item}")
    index += 1
print()

# item or i in lst is 3,79,793,1000
# index is 0,1,2,3

for index,item in enumerate(lsts):
    print(f"The index {index} & it's item {item}")