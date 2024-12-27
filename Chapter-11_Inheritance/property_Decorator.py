class Emp:
    a = 1
    @classmethod
    def show(cls):
        print(f"The Class Attributes of 'a' is : {cls.a}") # Output : 1
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
    
e = Emp()
e.a = 10
e.name = "Mahy's Bgu"
print(e.name)
print(e.fname)
print(e.lname)
e.show()