'''Create a class "Programme" for storing information of few programers 
working at Microsoft'''

class Programme:
    company = "Microsoft"
    def init_(self, name, sal, degn):
        self.name = name
        self.sal = sal
        self.degn = degn
    
p = Programme()
p.name = "Mahy"
p.sal = 300000
p.degn = "Developer"
print(p.name, p.sal, p.degn, p.company) 

b = Programme()
b.name = "Mahi"
b.sal = 213000
b.degn = "Data Scientist"
print(b.name, b.sal, b.degn, b.company) 