'''Write a class Train which has methods to book a ticket, get 
status(no of Seats) & get Fare info of train running under 
Indian Railway.'''

from random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
    def book(self, frum, to):
        print(f"Ticket is Booked in Train no : {self.trainNo} from {frum} to {to}")
    
    def getStatus(self):
        print(f"Train No : {self.trainNo} is running on Time")

    def getFare(self, frum, to):
        print(f"Ticket Fare in Train no : {self.trainNo} from {frum} to {to} is {randint(222, 5555)}")

t = Train(123008)
t.book("Cuttack", "Bangalore")
t.getStatus()
t.getFare("Cuttack","Bangalore")