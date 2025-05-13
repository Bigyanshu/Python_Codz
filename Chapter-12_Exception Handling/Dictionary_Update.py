# Dictionary Merge & Update Operator

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3 , 'd': 4}
# b Value is updated here only
merged = dict1 | dict2

print(merged)  # Output : {'a': 1, 'b': 3, 'c': 3, 'd': 4}



# with (
#     open('files1.txt') as f:
#     open('files2.txt') as f
#     ):
#     f.write(dict1 + dict2)  
