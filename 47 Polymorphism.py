class Bird:
    def sound(self):
        print("Bird sound")

class Crow(Bird):
    def sound(self):
        print("Crow caws")

b = Crow()
b.sound()
