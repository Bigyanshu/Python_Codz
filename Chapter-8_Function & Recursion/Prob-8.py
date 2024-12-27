# WA python function to print multiplication table with forwards & Backwards
def mul(n):
    for i in range( 11 ):
        print(f"{n} x {i} = {n*i}")
num = int(input("Enter a Number : "))
mul(num)

#Reverse
def rev_mul(n):
    for item in range(11):
        print(f"{n} x {11-item} = {n*(11-item)}")
no = int(input("Enter a No : "))
rev_mul(no)