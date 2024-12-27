# Multiplication Table in for loop 

n = int(input("Enter the number: "))

for i in range (1,n+2): # (1,11)
    print(f"{n} * {i} = {n * i}")

'''
Enter the number: 9
9 * 1 = 9
9 * 2 = 18
9 * 3 = 27
9 * 4 = 36
9 * 5 = 45
9 * 6 = 54
9 * 7 = 63
9 * 8 = 72
9 * 9 = 81
9 * 10 = 90
'''

# Multiplication Reverse order table with for loop 

n = int(input("Enter the number: "))

for i in range(1, 11):
    print(f"{n} * {i} = {n * i}")


"""
9*10=90
9*9=81
9*8=72
9*7=63
9*6=54
9*5=45
9*4=36
9*3=27
9*2=18
9*1=9
"""