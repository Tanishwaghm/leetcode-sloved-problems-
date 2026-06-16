class Car:
    brand = "BMW"   # class variable

    def __init__(self, model):
        self.model = model  # instance variable

c1 = Car("X5")
c2 = Car("X7")

print(c1.model, c2.model)
print(Car.brand)
