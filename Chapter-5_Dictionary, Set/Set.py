p = () #Empty set
l = {} #Empty dictionary not empty set

s= {1,3,7,9,11,3,9,7,4.,6.8,8,"Mahy", 'Mahi'}
s.add(14)
print(s,type(s)) # Outputs: How varries, explain...?
        # Due to set has no indexing format

        #{1, 3, 4.0, 6.8, 7, 8, 9, 11, 'Mahy', 14, 'Mahi'}
        #{1, 3, 4.0, 6.8, 7, 8, 9, 'Mahy', 11, 14, 'Mahi'}
        #{1, 3, 4.0, 'Mahy', 6.8, 7, 8, 9, 'Mahi', 11, 14}
        #{1, 3, 4.0, 6.8, 7, 8, 9, 11, 14, 'Mahy', 'Mahi'}
        #{1, 3, 4.0, 'Mahy', 6.8, 7, 8, 9, 11, 14, 'Mahi'}

# print(s.add(14)) # Output : None

print(len(s)) # Outputs: 11 ,not 13 due to set has unique values so it eliminate duplicates

# Set methods
d = {1,2,3,4}
e = {4,5,9}

# Union
print(d.union(e)) # Output : {1, 2, 3, 4, 5, 9}

# Intersection
print(d.intersection(e)) # Output : {4}

# Difference : Set has unique values so it calculate Unique & eliminate duplicates
print(d.difference(e)) # Output : {1, 2, 3}
print(e.difference(d)) # Output : {9, 5}

# Symmetric Difference : Returns new set containig elements that are in either of sets but not in both.
print(d.symmetric_difference(e))
print(e.symmetric_difference(d))

# issubset():
s1 = {1,2,3,4}
s2 = {1,2,3,4,5,6,8,9}
print(s1.issubset(s2)) # Output : True
print(s2.issubset(s1)) # Output : False

# issuperset():
print(s1.issuperset(s2)) # Output : False
print(s2.issuperset(s1)) # Output : True

# isdisjoint(): The isdisjoint() method checks whether two sets have no elements in common. If the two sets have no common elements, the method returns True. If there is at least one common element, it returns False.
c = {1,2,3,4}
g = (6,7,8,9)
print(s1.isdisjoint(s2)) # Output : False
print(c.isdisjoint(g)) # Output : True
