# WA recursive function to calculate the sum of the n nos\
# sum(n) = 1+2+3+...+(n-1)+n   formulae
def sum(n):
    if n ==1:
        return 1
    else:
        return sum(n-1) + n
    
z = int(input("Enter a NO. : "))
print(sum(z))