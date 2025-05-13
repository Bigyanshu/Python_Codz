class Human:    
#class variables
    populations = 0
    data = []
    Human = 100

    # Constructor
    def __init__(self, name, age, alive = True):
        self.name = name
        self.age = age
        self.alive = alive

        # increment the population
        Human.populations += 1
        Human.data.append(self.name)

    #Method
    def greet(self):
        print(f"Hello my name is {self.name}. Good Mornings !")

    def dead(self):
        print(self.name, "is no more now")
        Human.populations -= 1

    h1 = Human("H1", 80)
    h2 = Human("H2", 90)

    # Human,populations
    h1.dead()
Human.populations()
