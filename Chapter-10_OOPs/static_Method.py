class Employee:
    name = 'Mahy' # These 3 are class attributes
    lang = 'Python'
    sal = 213000
    def getInfo(self):
        print(f"The Langage is : {self.lang} & Getting  salary : {self.sal}")
    @staticmethod
    def greets():
        print("Welcome to the Oops of Python")
bgu = Employee()
bgu.name = 'Mahi' # These object / instance attributes & More priors than the class attributes
bgu.lang = 'React' # These object / instance attributes & More priors than the class attributes

#Function Callings
# bgu.getInfo()
bgu.greets()
Employee.getInfo(bgu)