'''WAP to display a/b where a & b are interger. If b=0, display infinite by 
handling 'ZeroDivisionError'.'''

try:
     a = int (input("Enter a number: "))
     b = int (input("Enter another number: "))
     print(f"a/b is {a/b}")
except ZeroDivisionError as z:
    print("Infinite")    