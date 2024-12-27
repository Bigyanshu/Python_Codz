class Emp:
    a = 1
    def show(self):
        print(f"The Class Attributes of a is : {self.a}") # Output : 10
    
e = Emp()
e.a = 10
e.show() # Due to instance variables prefer more priority than class attributes

# But How give More priority to Class Attributes
class Emp:
    a = 1
    @classmethod
    def show(self):
        print(f"The Class Attributes of a is : {self.a}") # Output : 1
    
e = Emp()
e.show()
e.a = 10