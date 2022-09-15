# In-class examples

# name = input('What is your name? ')
name = 'Randy'
# age_str = input('How old are you? ')
age_str = "47"
age = int(age_str)

print(name)
print('name:', name)
print(name, age)
print(name, age, sep = '/', end = '\n\n\n') # gross
print(name + '/' + str(age) + '\n\n')       # even grosser

output_message = f'My name is {name}, and I am {age + 10} years old.'
print(output_message)

print(f'{age}')
print(f'{age = }')

class_average = (65.0 + 52.5 + 73.5) / 3

print(f'{class_average}')
print(f'{class_average:.2f}')

first_name = 'Randy'
last_name = 'Fortier'
full_name = first_name + last_name
print(full_name)

print(True and False) # &&
print(True or False)  # ||

full_name_type = type(full_name)
print(full_name_type)

print(type(class_average))

# Hackers' corner

first_name = 'Rhonda'
age = 21

output_message = f'My dogs name is {first_name}, and I am {age} years old.'
output_message = f'Your name is {first_name}, and I am {age} years old.'
output_message = f'Her name is {first_name}, and I am {age} years old.'
output_message = f'Their name is {first_name}, and I am {age} years old.'
output_message = f'My name is {first_name}, and I am {age + 10} years old.'
output_message = f'My name is {first_name}, and I am {age + 10} years old.'
output_message = f'My name is {first_name}, and I am {age + 10} years old.'
output_message = f'My name is {first_name}, and I am {age + 10} years old.'
output_message = f'My name is {first_name}, and I am {age + 10} years old.'

# Coding exercise

import turtle 

window = turtle.Screen()

t = turtle.Turtle()

t.pendown()

step = 50
angle = 90

t.forward(step)
t.right(angle)
# step = step + 10
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

t.forward(step)
t.right(angle)
step += 10
angle -= 5

t.penup()

window.mainloop()

# Coding challenge (initially centered, facing right)

