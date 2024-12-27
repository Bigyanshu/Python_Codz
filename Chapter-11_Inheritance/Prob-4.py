'''WA class "Complex" to represent complex no salary with overloaded operators 
'+' & '*' which adds & multiplies them'''

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
        
    def __add__(self, c2):
        return Complex( self.real + c2.real, self.imag + c2.imag )
    
    def __mul__(self, c2):
        real_part = self.real * c2.real + self.imag * c2.imag
        imag_part = self.real * c2.real - self.imag * c2.imag
        return Complex (real_part, imag_part)
    
    def __str__(self):
        return f'{self.real}  {self.imag}i'
    
c1 = Complex(3,5)
c2 = Complex(7,9)
print("Addition       :", c1 + c2)
print("Multiplication :", c1 * c2)