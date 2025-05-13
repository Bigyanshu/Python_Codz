"""
Print This type pattern

*
***
*****

"""
n = int (input('Enter a Num : '))

for i in range(1, n+1):
    print("*" * (2*i-1), end = "")
    print(" ")


"""
Print This type pattern

*
**
***

"""
n = int (input('Enter a Num : '))

for i in range(1, n+1):
    print("*" * i, end = "")
    print(" ")

"""
Print This type pattern

*    *
**  **
******

"""
n = int (input('Enter a Num : '))

for i in range(1, n+1):
    if(i == n): 
        print("*"* n, end = "")
    else:
        print("*"* (2*i), end = "")
        print(" "* (2*n-2*i), end = "")
        print("")