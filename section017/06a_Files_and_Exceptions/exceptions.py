x = 3
names = ['Bob', 'Carla', 'Joanne']

try:
    print(names[x])
    z = x / 0
except ZeroDivisionError as e:
    print(f'Error when dividing by zero: {e}')
except IndexError as e:
    print(f'Error when indexing the names array: {e}')

print('after the exception')

class InvalidKnightMove(Exception):
    pass 

try:
    move_x = int(input('X coordinate:'))
    move_y = int(input('Y coordinate:'))
    if move_x < 0 or move_y < 0:
        raise InvalidKnightMove(f'Your knight cannot move to {move_x}, {move_y}')
except InvalidKnightMove as error:
    print(error)

print('Ask the user to enter new coordinates')

