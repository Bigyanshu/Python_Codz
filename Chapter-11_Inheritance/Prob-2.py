# Create a class 'Pets' from a class 'Animals' and further create a class
#  'Dog' from 'Pets'. Add a method bark to class Dog

class Animals:
    pass

class Pets (Animals):
    def cat(self):
        print ("Meun Meun")

class Dog (Pets):
    @staticmethod 
    def bark():
        print ("Vow Bow")

d = Dog() 
d.bark()

c = Pets()
c.cat()