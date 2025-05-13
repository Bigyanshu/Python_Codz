# If the names of 2 friends are same; what will happen to the program in problem 6 ?

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

print(s) 
''' Output : {'Bgu': 'Python', 'Omny': 'Data Analytics', 'Mahi': 'Data Science'}
Duplicate Friends Names language changed which is entered lastly'''