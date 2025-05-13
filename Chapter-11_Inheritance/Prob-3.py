'''Create a class employee & add salary & increament properties to it.
WA methods 'salAfterIncreament' method with a @properties decorator with a 
setter which changes value of increament based on salay.'''


class Employee:
    sal = 230  # Initial salary
    incr = 20  # Initial increment percentage

    @property
    def salAfterIncreament(self):
        # Salary after increment = salary + (salary * increment percentage)
        return self.sal + (self.sal * self.incr / 100)

    @salAfterIncreament.setter
    def salAfterIncreament(self, salary):
        # Calculate new increment based on the updated salary
        self.incr = ((salary / self.sal) - 1) * 100

e = Employee()
print("Salary After Increament : ",e.salAfterIncreament)  # Step 1: Print salary after applying increment
# e.salAfterIncreament = 280.0  # Step 2: Set new salary as 280.0
print("Increament is : ",e.incr)  # Step 3: Print the new increment percentage

# Another Way
'''class Employee:
    sal = 213
    incr = 20

    @property
    def salAfterIncreament(self):
        return (self.sal+ self.sal*(self.incr))
    
    @salAfterIncreament.setter
    def salAfterIncreament(self, salary):
        self.incr = ((salary/self.sal)-1)*100

e = Employee()
print(e.salAfterIncreament)
e.salAfterIncreament = 280.0
print(e.incr)'''