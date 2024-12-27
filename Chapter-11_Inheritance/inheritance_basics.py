# nheritance

class Emp:
    a = 1
class Prog(Emp):
    b = 2
class Mgmt(Prog):
    c = 3
e = Emp()
print ("Emp  : ",e.a)
print()

p = Prog()
print ("Prog : ",p.b)
print ("Prog : ",p.a)
print()

m = Mgmt()
print ("Mgmt : ",m.a)
print ("Mgmt : ",m.b)
print ("Mgmt : ",m.c)