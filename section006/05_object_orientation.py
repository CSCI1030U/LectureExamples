# classes, objects, methods, instance variables

class Pet:
    def __init__(self, name, age, breed, colours, sex):
        # self - a variable containing the instance
        self._name = name
        self._pets_age = age
        self._breed = breed 
        self._colours = colours 
        self._sex = sex
    
    # accessor (getter)
    def get_name(self):
        return self._name
    
    # mutator (setter)
    def set_name(self, new_name):
        self._name = new_name

    def __str__(self):
        return f'Pet(name={self._name}, breed={self._breed})'

class Dog(Pet):
    def bark(self):
        print('bark bark bark')

# Pet -> Dog -> Rotweiller
class Rotweiller(Dog):
    pass

class Cat(Pet):
    def meow(self):
        print('meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow')

lenny = Cat('Lenny', 1, 'Domestic Long-haired Cat', 'Orange/White', 'Male')
# print(lenny._name)  # legal, but not recommended (bad practice accessing private variables outside of the class)
print(lenny.get_name())
# lenny.bark()  # no bark() method on Pet class
lenny.meow()

print(lenny)  # => print(str(lenny))

spike = Dog('Spike', 4, 'Rotweiller', 'Black/Brown', 'Female')
spike.bark()