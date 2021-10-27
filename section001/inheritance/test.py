from dog import Dog 
from cat import Cat

dragon = Dog('Dragon', 10.0)
milo = Dog('Milo', 3.0)

print(dragon.get_name())
print(milo.get_name())

zeke = Cat('Zeke', 4.0)
turbo = Cat('Turbo', 1.5)

print(f'First cats name: {zeke.get_name()}')
print(f'Second cats name: {turbo.get_name()}')

if dragon < milo:
    print('Dragon is the smaller dog')
else:
    print('Milo is the smaller dog')