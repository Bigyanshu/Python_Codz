'''WAP to filter a list of number which are divisible by 5'''

def divisible5(n):
    if n % 5 == 0:
        return True
    return False

numbers = [2, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 85, 90, 95]
f = list(filter(divisible5, numbers))
print("Divisible by 5 are : ",f)