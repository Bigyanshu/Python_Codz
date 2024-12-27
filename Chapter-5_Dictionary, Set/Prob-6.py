'''Create an empty dictionary. Allow 4 friends to enter their favorite language as
value and use key as their names. Assume that the names are unique '''

s = {}

name = input('Enter your one friend Name : ')
lang = input('Enter thier favorite language : ')
s.update({name : lang})

name = input('Enter your one friend Name : ')
lang = input('Enter thier favorite language : ')
s.update({name : lang})

name = input('Enter your one friend Name : ')
lang = input('Enter thier favorite language : ')
s.update({name : lang})

name = input('Enter your one friend Name : ')
lang = input('Enter thier favorite language : ')
s.update({name : lang})

print(s) # Output : 