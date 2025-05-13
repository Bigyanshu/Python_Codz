friends = ['Apple', 'Orange', 5, 345.06, False, 'Mahy', 'Omny']
print(friends[0])

friends[0] = "Grapes"
print(friends[0])

print(friends[1:5])

friends.append("Omnypotent")
# print(friends.append("Omnypotent")) # Output: None
print(friends)

lst =[3,7,21,9,12]
# print(lst.sort()) # Output: None
lst.sort()
print(lst) # Output:  [3, 7, 9, 12, 21]


lst.sort(reverse=True) # Output
print(lst) # Output: [21, 12, 9, 7, 3]

lst.reverse()
print(lst) # Output:  [3, 7, 9, 12, 21]

lst.insert(4,97)
print(lst) # Output:  [3, 7, 9, 12, 97, 21]

v = lst.pop(3)
print(lst) # Output:  [3, 7, 9, 97, 21]
print(v) # Output: 12

lst1 = [7, 9, 97, 21, 9, 9,]
kl = lst1.remove(9)
print("List :",lst1) # Output:  List : [7, 97, 21, 9, 9]

lst1.count(9)
print("List Count :",lst1)

lst1.clear()
print(lst1)

lst.extend([29,77])
print(lst)

# lst = [1, 3, 4, 9]
index = lst.index(9)  # Output: 1
print(index)

print(max(lst))
print(min(lst))

print(lst) # Output: [3, 7, 9, 97, 21, 29, 77]