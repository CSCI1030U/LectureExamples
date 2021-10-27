# classes, methods, instance variables, inheritance

class Pet:
    def __init__(self, name, breed, health, mass):
        # _ prefix means 'private'
        self._name = name
        self._breed = breed
        self._health = health 
        self._mass = mass 
        self._num_visits = 0

    # accessor (read the value of an instance variable)
    def get_name(self):
        return self._name

    # mutator (set the value of an instance variable)
    def set_name(self, new_name):
        self._name = new_name
    
    def feed(self, amount):
        self._mass += amount

    def __str__(self):
        return f'Pet({self._name}, {self._breed})'


spot = Pet('Spot', 'Poodle', 100, 2.1) # create an instance
boots = Pet('Boots', 'Domestic Cat', 80, 1.4)

# print(boots._name)   # should never happen (bad practice to access private variables external to the class)
print(boots.get_name())

print(spot)

# from section017:
# inheritance/cat.py

# from re-recordings:
# ../section017/inheritance/cat.py

# absolute:
# C:/CSCI1030U/LectureExamples/section017/inheritance/cat.py