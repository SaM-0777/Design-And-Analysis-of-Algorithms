class Animal(object):
    legs = 4
    def __init__(self, name):
        self.Name = name
    print(legs)

A = Animal("Lion")
print(A.legs)
A.legs = 8
print(A.legs)

class Human(Animal):
    print(Animal.legs)