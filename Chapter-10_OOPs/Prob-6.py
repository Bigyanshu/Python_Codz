'''Can you change self-parameters inside a class to somethhing else
(say "bgu"). Try changing self to 'slf' or 'bgu' & see the effects'''

from random import randint

class Train:
    def __init__(elf, trainNo):
        elf.trainNo = trainNo
    def book(bgu, frum, to):
        print(f"Ticket is Booked in Train no : {bgu.trainNo} from {frum} to {to}")
    
    def getStatus(self):
        print(f"Train No : {self.trainNo} is running on Time")

    def getFare(slf, frum, to):
        print(f"Ticket Fare in Train no : {slf.trainNo} from {frum} to {to} is {randint(222, 5555)}")

t = Train(123008)
t.book("Cuttack", "Bangalore")
t.getStatus()
t.getFare("Cuttack","Bangalore")