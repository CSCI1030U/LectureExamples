from cat import Cat 
from dog import Dog

lenny = Cat('Lenny', 1.4)
chowder = Dog('Chowder', 3.4)
pupcake = Dog('Pupcake', 12.0)

if chowder < pupcake:
    print('Chowder is just a teeny dog compared to Pupcake')
else:
    print('Chowder towers over Pupcake')
