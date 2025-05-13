# Factorial 

n =  int(input('Enter a number : ')) #5
prod = 1

for i in range(1,n+1):
    prod = prod * i
print(f"Facrorial of {n} is {prod}")