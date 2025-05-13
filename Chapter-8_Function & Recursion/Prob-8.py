# WA python function to print multiplication table with forwards & Backwards
def mul(n):
    for i in range( 11 ):
        print(f"{n} x {i} = {n*i}")
        
num = int(input("Enter a Number : "))
mul(num)

#Reverse
def rev_mul(n):
    for item in range(11):
        print(f"{n} x {10-item} = {n*(10-item)}")

no = int(input("Enter a No for reverse mul : "))
rev_mul(no)