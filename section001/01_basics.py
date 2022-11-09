# Basics
from pdb import line_prefix


x = 1  # y = 2
'''
This is a line
Another line
'''

name = 'Randy' # input("Enter your name: ")
age_str = '47' # input("How old are you? ")
age = int(age_str)

print(name, age)
print(name, age, sep='***', end='\n\n\n')

print(f'My name is {name} and I am {age} years old.')

average = (55.0 + 62.0 + 71.5) / 3
print(f'{average = }')
print(f'{average:.2f}')

full_name = 'Randy' + 'Fortier'
print(f'{full_name = }')

print('abc ' * 5)
print('*' * 50)

print(True and False)
print(True or False)

full_name_type = type(full_name)
print(f'{full_name_type = }')

# Hackers' corner

fname = 'Randy'
age = 47

print(f'My name is {fname} and I am {age} years old.')
print(f'My name is {fname} and I am {age} years old.')
print(f'My name is {fname} and I am {age} years old.')
print(f'My name is {fname} and I am {age} years old.')
print(f'My name is {fname} and I am {age} years old.')
print(f'My name is {fname} and I am {age} years old.')
print(f'My name is {fname} and I am {age} years old.')

# Coding exercise 1.1

import turtle

window = turtle.Screen()
t = turtle.Turtle()
t.pendown()

# facing right, centre of screen

step = 50
angle = 90

t.forward(step)
t.right(angle)
step += 10 #step = step + 10
angle -= 5

t.forward(step)
t.right(angle)
step += 10
angle -= 5

t.forward(step)
t.right(angle)
step += 10
angle -= 5

t.forward(step)
t.right(angle)
step += 10
angle -= 5

t.forward(step)
t.right(angle)
step += 10
angle -= 5

t.forward(step)
t.right(angle)
step += 10
angle -= 5

t.forward(step)
t.right(angle)
step += 10
angle -= 5

t.forward(step)
t.right(angle)
step += 10
angle -= 5

t.forward(step)
t.right(angle)
step += 10
angle -= 5

t.forward(step)
t.right(angle)
step += 10
angle -= 5

t.forward(step)
t.right(angle)
step += 10
angle -= 5

t.forward(step)
t.right(angle)
step += 10
angle -= 5

t.forward(step)
t.right(angle)
step += 10
angle -= 5

t.forward(step)
t.right(angle)
step += 10
angle -= 5

t.forward(step)
t.right(angle)
step += 10
angle -= 5

t.forward(step)
t.right(angle)
step += 10
angle -= 5

window.mainloop()



# Coding challenge (initially centered, facing right)
