'''Stored multiplication tables gemerated in prob-3 in a file named Table.txt'''

n = int(input("Enter a Number: "))
table = [n * i for i in range (1,11)]
with open ("Table.txt", 'a')as f:
    print(f.write(f"Table of {n} : {str(table)}\n"))
    print(type(table))