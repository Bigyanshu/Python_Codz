# Syntax of Advanced Type_Definitions
# Here we can import list, tuple, dict and union typing modules

from typing import List, Tuple, Dict, Union

# List Integers
numbers : List[int] = [1,3,5,7,9]
print(numbers)

# Tuple of Integers and Strings
coordinates : Tuple[int, int, str] = (10, 20, "coordinates")    
persons : Tuple[str, int] = ('Mahy', 10)
print(coordinates, persons)

# Dictionary with String keys and Interger values
scores : Dict[str, int] = {"Mahy": 99, 'Mahi': 97}
print(scores)

# Union type for variables that can hold multiple types
identifies : Union[int, str] = "ID973"
identifiers = 13579
identifiers2 = "Mahy"

print(identifies)
print(identifiers)
print(identifiers2)