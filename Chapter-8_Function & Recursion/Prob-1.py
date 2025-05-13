# find greatest of three no using function
def gratest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c :
        print(f"Greatest no is : {b}")
    elif c>a and c>b:
        print(f"Greatest no is : {c}")
    
a = int(input("Enter a No: "))
b = int(input("Enter b No: "))
c = int(input("Enter c No: "))

print(gratest(a,b,c))