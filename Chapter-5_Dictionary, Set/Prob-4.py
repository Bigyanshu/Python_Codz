'''What will be the length of following set s:
s = set() 
s.add(20)
s.add(20.0) 
s.add('20') # length of s after these operations? '''

s = set() 
s.add(20)
s.add(20.0) 
s.add('20')

print(len(s)) # Output : 2 not 3
''' 20 (integer) and 20.0 (float) are considered equal, so only one of them is added 
to the set.
'20' (string) is a unique element and is added to the set.
As a result, the final set contains 2 elements, and the length of the set is 2.'''