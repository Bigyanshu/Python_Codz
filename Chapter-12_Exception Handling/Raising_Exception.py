x = int ( input ("Enter a number: "))
y = int ( input ("Enter another number: "))

if (y == 0) :
    raise ZeroDivisionError ("Any No. can't devide by zero")
else:
    print(f"Division of x/y is : {x/y}", type(x/y))
# z = x/y
# print(z, type(z))