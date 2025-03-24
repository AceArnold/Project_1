print("Hello world")

class Passenger:
    def __init__(self, person, weight):
        self.person = person
        self.weight = weight
    def adding_passenger(self):
        passengers=[]
        if self.weight > 46:
            print("You are too heavy to ride")
        else:
            print("Welcome to the flight")
            passengers.append(self.person)
        

x=Passenger(john, 4)
x.adding_passengers
print(x)
 