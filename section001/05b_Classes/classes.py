class Pet:
    def __init__(self, species, name):
        self.species = species
        self.name = name
        self.fluffiness = 0.6

    def set_fluffiness(self, fluff):
        self.fluffiness = fluff
    
    def __str__(self):
        return f'{self.name} ({self.species})'
    
    def __lt__(self, other):
        return self.fluffiness < other.fluffiness


# this does these two things:
# 1. creates a new instance of Pet
# 2. initializes that Pet instance (constructor)
spot = Pet('Dog', 'Spot')
mittens = Pet('Cat', 'Mittens')
mittens.set_fluffiness(0.9)
print(spot)
print(mittens)

spot_str = str(spot)
if spot < mittens:
    print('Spot is not as fluffy as mittens')

class Dog(Pet):
    def __init__(self, name, breed):
        super().__init__('Dog', name)
        # these two are equivalent
        # Pet.__init__(self, 'Dog', name)

        self.breed = breed 
    
    def set_breed(self, breed): # mutator
        self.breed = breed 
    
    def get_breed(self):        # accessor
        return self.breed 

    def speak(self):
        return 'Arf arf!'

pedro = Dog('Pedro', 'Rotweiller')
print(pedro.speak())

# programming exercise
## Iterators
class PerfectSquares:
    '''
    PerfectSquares

    This is an iterator for all perfect square positive integers.
    '''
    def __init__(self):
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        return self.current**2

print('Perfect squares less than or equal to 100:')
perfectSquares = PerfectSquares()
for num in perfectSquares:
    if num <= 100:
        print(num)
    else:
        break
    
