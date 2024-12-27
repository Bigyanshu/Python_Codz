'''Write __str__() method to print vector as follows:
7i + 8j + 10k
Assume vector is 3d'''

class Vector:
    def __init__(self, list):
        self.list = list
        # pass
    def __add__(self, other):
        result = Vector( self.x + other.x, self.y + other.y, self.z + other.z)
        return result
    
    def __mul__(self, other):
        result = (self.x * other.x + self.y * other.y+ self.z * other.z)
        return result
    
    def __str__(self):
        return f"{self.x}, {self.y}, {self.z}"
    
    def __len__(self):
        return 3
    # pass

# Same Dimension Vectors   
v1 = Vector([1, 3, 7])  # Vector with components (1, 2, 3)

# Test vector addition and dot product
print(len(v1))  # Output: Vector(5, 7, 9)


# Anothor Way

class Vector:
    def __init__(self, list):
        self.list = list
    
    def __len__(self):
        return len(self.list)

v1 = Vector([1,3,5])
print(len(v1))