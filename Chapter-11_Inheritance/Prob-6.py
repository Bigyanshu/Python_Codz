'''Write __str__() method to print vector as follows:
7i + 8j + 10k
Assume vector is 3d'''

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, other):
        result = Vector( self.x + other.x, self.y + other.y, self.z + other.z)
        return result
    
    def __mul__(self, other):
        result = (self.x * other.x + self.y * other.y+ self.z * other.z)
        return result
    
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"

# Same Dimension Vectors   
v1 = Vector(3, 3, 4)  # Vector with components (1, 2, 3)
v2 = Vector(4, 5, 6)  # Vector with components (4, 5, 6)
v3 = Vector(7, 8, 9)  # Vector with components (7, 8, 9)

# Test vector addition and dot product
print(v1 + v2)  # Output: Vector(5, 7, 9)
print(v1 * v2)  # Output: Dot product (32)
print(v1 + v3)  # Output: Vector(8, 10, 12)
print(v1 * v3)  # Output: Dot product (50)