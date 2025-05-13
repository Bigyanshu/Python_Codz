'''Crerate a class 2d vector & use it to create another 
class representing a 3d Three_D_Vector'''

class Two_D_Vector:
    pass
    def __init__(self,i,j):
        self.i = i
        self.j = j
    def show(self):
        print(f"Vector is : {self.i}i+{self.j}j")
class Three_D_Vector(Two_D_Vector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k
    def show(self):
        print(f"Vector is : {self.i}i+{self.j}j+{self.k}k")
n = Two_D_Vector(1,2)
m = Three_D_Vector(3,7,9)

n.show()
m.show()