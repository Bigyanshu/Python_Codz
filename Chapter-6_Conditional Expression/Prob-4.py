# User name contain 10 characters or not

UName = input("User Name Enter: ")

if(len(UName) < 10):
    print("User Name contain less than 10 characters.")
else:
    print("User Name contain 10 characters or more.")