# WAP to find greatest of 4 no entered by user

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))

if(num1 > num2 and num1 > num3 and num1 > num4):
    print("Greater Number is num1:", num1)
elif(num2 > num1 and num2 > num3 and num2 > num4):
    print("Greater Number is num2:", num2)
if(num3 > num1 and num3 > num2 and num3 > num4):
    print("Greater Number is num3:", num3)
if(num4 > num1 and num4 > num2 and num4 > num3):
    print("Greater Number is num4:", num4)