'''Write a class "Calculator" capable of finding square, cube & squareroot of a number'''

class Calculator:
    def _init_(self,n=4):
        self.n = n
    def square(self):
        print(f"The Square is : {self.n * self.n}")
    def cube(self):
        print(f"The Cube is : {self.n * self.n * self.n}")
    def squareroot(self):
        # print(f"The Square root is : {self.n * 1/2}")
        print(f"The Square root is : {self.n * 0.5}")

c = Calculator()
c.n = 4
c.square()
c.cube()
c.squareroot()