# Can you change the values inside a list which is contained in set S?

# Answers

s = {8, 7, 12, "Harry", [1,2]}

''' No, you cannot change the values inside a list [1,2] that is contained in a set.
In fact, you cannot even add a list to a set in the first place. The reason is 
that sets in Python require all of their elements to be hashable and immutable.'''

# Alternate Solution
'''If you need to store a collection of items inside a set,
consider using a tuple instead of a list, as tuples (1,2) are immutable and hashable.'''

s = {8, 7, 12, "Harry", (1, 2)}
