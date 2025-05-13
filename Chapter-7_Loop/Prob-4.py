n = int(input("Enter a Num : "))

if n < 2:
    print(f"{n} is not a prime number.")
    
elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
    print("Not a Prime Number...!")

elif n == 2:
    print(f"{n} is a prime number.")

else:
    print("Prime Number is", n)
