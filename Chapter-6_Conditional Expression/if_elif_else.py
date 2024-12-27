a = int(input("Enter your age: "))

if(a >= 18):
    print("You are an adult.",a)
elif(a <0 ):
    print("Invalid or Negative age",a)
elif(a ==0):
    print("Your age is 0\nYou are a kid.",a)
else:
    print("You are Minor",a)