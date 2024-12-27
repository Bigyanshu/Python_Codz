# Type_Definition hints (:) colon for variables
# Type_Definition hints (->) colon for functions

# Variable type hints
age: int = 17
print("Age : ",age,type(age))

# Function type hints
def greeting(name : str ) -> str :
    return f"Hello, {name}"

print (greeting("Mahy"))
print (greeting("Mahi"))