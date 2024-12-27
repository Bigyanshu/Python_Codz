'''WAP to input name, marks & phone numbers of a student & format it 
using format function like below :

"The name of the student is Mahy, his mark is 79 and phone no is 8260603905"
'''

name = input("Enter Name : ")
marks = int (input("Enter Mark: "))
phone = int (input("Enter Phone: "))

print("The name of the student is {0}, his mark is {1} and phone no is {2}".format(name,marks,phone))
