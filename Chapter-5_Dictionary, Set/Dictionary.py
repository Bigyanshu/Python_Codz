marks = {
    "Mahy": 90,
    "Mahi": 85,
    "Bgu": 95,
    "Pagu": 92,
    "BDpty": 88
}
print(marks,type(marks))
print(marks["Mahy"])

print(marks.items())
print(marks.update({"BDpty":99, "Pagu":97,"Babulyu":9, "Pragyan":98}))
print(marks)

print(sorted(marks.keys()))
print(sorted(marks.values()))

print("Keys are:",marks.keys())
print("values are:",marks.values())

# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'b': 2, "Mahy":100}
k = {'a': 1, 'b': 2, 'c': 3, 'b': 1, "Mahy":100}
value = k.get('c', 0)  # Returns 0 because 'c' is not a key in d
print(value)
v = k.get('b')  
v = k.get('a')  # Returns 1
print(v)# Returns 1 of a,because same variable name at calling time last element always called

w = k.pop('Mahy')
print(w) # Returns 100 due to b is removed from d.
print("Variable k:",k) #{'a': 1, 'b': 1, 'c': 3}

z = k.popitem() #('c',3) is removed from d
z = k.popitem() #('b',1) is removed from d
z = k.popitem() #('a',1) is removed from d
print(z) # Returns ('c', 3) because c is removed from d.
print(k) # Returns {} due to k variable has no element.
print(z) # it show recently whic was removed from variable

l = {'a': 4, 'b': 2, 'c': 3, 'a': 3, "Mahy":100, 'l': 2,}
print(l.pop("l"))
print(l.popitem())
print("Variable l:",l)
# print(l.clear())
print("Variable l 2nd:",l)

n = l.setdefault("m",23)
print(n) #
print(l) #

d = {'a': 1, 'b': 2}
copy_d = d.copy()  # Creates a shallow copy of d
print(copy_d) # Returns