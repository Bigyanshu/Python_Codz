# Inches to cms
def inches_to_cms(inch):
    return inch * 2.54
n = int(input("Enter the number in inches : "))
print(f"Value {n} in cms is {(inches_to_cms(n))}")