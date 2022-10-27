# coding challenge (Dog class)

class Dog:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def get_name(self):
        return self.name

    def get_mass(self):
        return self.mass

    def __str__(self):
        return f'{self.name} (mass: {self.mass})'

    def __lt__(self, other):
        return self.mass < other.mass

dog1 = Dog('Sparky', 5.0)
dog2 = Dog('Andre', 11.5)
print(f'{str(dog1) = }')
print(f'{str(dog2) = }')
print(f'{dog1 < dog2 = }')
