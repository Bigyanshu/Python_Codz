'''Create a class with a class attributes a create an object from it & set 'a' 
directly using deject.a=0. Does this change class attribute.'''

class Test:
    a = 10
    
o = Test()
# print(o) This line returns Memory Locations
print(  o.a )
o.a = 1
print(  o.a )
print(  Test.a )

# Hence this can't change class attributes