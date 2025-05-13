class Employee:
    name = 'Mahy' # These 3 are class attributes
    lang = 'Python'
    sal = 213000

    def __init__(self):  # _init_ is a duender method which is automatically called only
        print('Hey Mahy are you Ready for Ridings...!')
    def getInfo(self):
        print(f"The Langage is : {self.lang} & Getting  salary : {self.sal}")
    @staticmethod
    def greets():
        print("Welcome to the Oops of Python")

# Object Creation

bgu = Employee()
bgu.name = 'Mahi' # These object / instance attributes & More priors than the class attributes
bgu.lang = 'React' # These object / instance attributes & More priors than the class attributes
print(bgu.name, bgu.sal, bgu.lang)

#Function Callings

# bgu.greets()

# bgu.getInfo()
# Employee.getInfo(bgu)

p = Employee()
print("Q1")
print()

#2

class Emp:
    lang = 'Python' # These 3 are class attributes
    sal = 213000
    
    def __init__(self, name, sal, lang):  # _init_ is a duender method which is automatically called only
        self.name = name
        self.sal = sal
        self.lang = lang

        print('Hey Mahy are you Ready...!')

    def getInfo(self):
        print(f"The Langage is : {self.lang} & Getting  salary : {self.sal}")
    @staticmethod
    def greets():
        print("Welcome to the Oops of Python")

# Object Creation

bgu = Emp('Mahy', 3000000,'Python')
bgu.name = 'Mahi' # These object / instance attributes & More priors than the class attributes
bgu.lang = 'React' # These object / instance attributes & More priors than the class attributes
print(bgu.name, bgu.sal, bgu.lang)

#Function Callings

# bgu.greets()

# bgu.getInfo()
# Employee.getInfo(bgu)

p = Emp('Bgu',4000000, 'Next')
print(p.name, p.lang, p.sal)
