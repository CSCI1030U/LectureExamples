# Examples

# name = input('What is your name: ')
name = 'Randy'
# age_str = input('How old are you? ')
age_str = '47'
age = int(age_str)

print(name)
print('Name:', name)
print(name, age)

print(name + str(age))                   # yuck
print(name, age, sep = '', end = '\n\n') # blah

print(f'My name is {name} and I am {age - 20} years old.')

class_average = (65.0 + 48.0 + 77.0) / 3
print(f'Class average: {class_average}') 
print(f'{class_average=}')
print(f'{class_average = }')

output = f'{class_average:.2f}'
print(output)

first_name = 'Randy'
last_name = 'Fortier'
full_name = first_name + last_name
print(full_name)
print(f'{first_name} {last_name}')

class_avg_type = type(class_average)
print(class_avg_type)
print(type(full_name))

# Hackers' corner

first_name = 'Ronda'
age = 20

print(f'My name is {first_name} and I am {age} years young.')
print(f'My name is {first_name} and I am {age} years young.')
print(f'My first name is {first_name} and I am {age} years young.')
print(f'Her name is {first_name} and I am {age} years young.')
print(f'Their name is {first_name} and I am {age} years young.')
print(f'His name is {first_name} and I am {age} years young.')
print(f'My name is {first_name} and I am {age} years young.')
print(f'My name is {first_name} and I am {age} years young.')

# Coding exercise

import turtle 

window = turtle.Screen()

t = turtle.Turtle()

t.pendown()

step = 50
angle = 90

t.forward(step)
t.left(angle)
# step = step + 10
step += 10
angle -= 5

t.forward(step)
t.left(angle)
step += 10
angle -= 5

t.forward(step)
t.left(angle)
step += 10
angle -= 5

t.forward(step)
t.left(angle)
step += 10
angle -= 5

t.forward(step)
t.left(angle)
step += 10
angle -= 5

t.forward(step)
t.left(angle)
step += 10
angle -= 5

t.forward(step)
t.left(angle)
step += 10
angle -= 5

t.forward(step)
t.left(angle)
step += 10
angle -= 5

t.forward(step)
t.left(angle)
step += 10
angle -= 5

t.forward(step)
t.left(angle)
step += 10
angle -= 5

t.forward(step)
t.left(angle)
step += 10
angle -= 5

t.forward(step)
t.left(angle)
step += 10
angle -= 5

t.forward(step)
t.left(angle)
step += 10
angle -= 5

t.forward(step)
t.left(angle)
step += 10
angle -= 5

t.forward(step)
t.left(angle)
step += 10
angle -= 5

t.penup()

window.mainloop()

# Coding challenge (initially centered, facing right)

