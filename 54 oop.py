from abc import ABC, abstractmethod

class Vehicle(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):

    def start(self):
        print(self.name + " starts with key")

class Bike(Vehicle):

    def start(self):
        print(self.name + " starts with self kick")

c = Car("BMW")
b = Bike("Yamaha")

c.start()
b.start()
