# classes, objects, instance variables, methods, inheritance 

class Pet:
    # __abc__ is used when the function is a built-in
    def __init__(self, name, age, mass, colours, sex):
        self.name = name
        self.pet_age = age 
        self.mass = mass
        self.colours = colours
        self.sex = sex 
    
    def set_name(self, new_name):
        self.name = new_name
    
    def get_name(self):
        return self.name

    def __str__(self):
        return f'Pet({self.name}, {self.pet_age} yrs)'

lenny = Pet('Lenny', 1, 1.4, 'Orange/White', 'Male')
lenny.set_name('Leonardo')
print(lenny) # => print(str(lenny))

spot = Pet('Spot', 4, 3.5, 'Brown/Black', 'Female')
