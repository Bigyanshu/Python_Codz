'''Write a program to input eight numbers from the user and display all the unique numbers (once).'''
s = set()

n = input("Enter a number: ") # Entering no in string format
s.add(int(n)) # Convert in integer format

n = input("Enter a number: ")
s.add(int(n))

n = input("Enter a number: ")
s.add(int(n))

n = input("Enter a number: ")
s.add(int(n))

n = input("Enter a number: ")
s.add(int(n))

n = input("Enter a number: ")
s.add(int(n))

n = input("Enter a number: ")
s.add(int(n))

n = input("Enter a number: ")
s.add(int(n))

print(s) # Output : {1, 3, 4, 5, 6, 7, 8, 9}