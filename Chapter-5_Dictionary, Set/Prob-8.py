# If languages of two friends are same; what will happen to the program in problem 6?

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
''' Output : If entered Value are same then length will remain same 
{'Mahy': 'Python', 'Bgu': 'Java', 'Omny': 'Python', 'Puchky': 'C'}'''