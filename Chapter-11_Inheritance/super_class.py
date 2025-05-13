class Emp:
    def _init_(self):
        print("Constructor of Employee:")
    a = 1
class Prog(Emp):
    def _init_(self): # _init_() is a constructor & it calls constructor of Base class
        # super()._init_()
        print("Constructor of Programmer:")
    b = 2
class Mgmt(Prog):
    def _init_(self):
        super()._init_() # It return it's parent class i.e. Prog
        print("Constructor of Management:")
    c = 3

e = Emp()
print(e.a)
p = Prog()
print(p.b)
m = Mgmt()
print(m.c)