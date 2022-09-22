# practice

our_type = 'Fire'
enemy_type = 'Grass'

our_damage = 20

if our_type == 'Fire' and enemy_type == 'Fire':
    our_damage *= 0.5
elif our_type == 'Fire' and enemy_type == 'Water':
    our_damage *= 0.5
elif our_type == 'Fire' and enemy_type == 'Grass':
    our_damage *= 2.0

print(f'{our_damage = }')

n = 0
while n < 10:
    print(f'while loop {n}')

    n += 1

for n in [0,1,2,3,4,5,6,7,8,9]:
    print(f'for loop (list) {n}')

for n in range(10): # range(0, 10, 1)
    print(f'for loop (range) {n}')

for n in range(100, 0, -5):
    print(f'for loop (range with 3 args): {n}')

# hacker's corner

# unary (-7)
# binary (2 + 3)
# ternary (val1 if question else val2)

x,y = 4,-3

if x > y:
    max2 = x
else:
    max2 = y

max2 = x if x > y else y

print(f'{max2 = }')

gen1 = (x * 2 for x in [0,1,2,3])

# print(f'{gen1 = }')
for i in gen1:
    print(f'for gen1: {i=}')

gen2 = (n ** 2 for n in range(0, 10, 2))
for i in gen2:
    print(f'for gen2: {i=}')

# coding exercise

import math

x = 1
num_terms = 20
e_estimate = 0.0

for n in range(num_terms):
    numerator = x ** n 
    denominator = math.factorial(n)
    e_estimate += numerator / denominator

    print(f'{e_estimate = }')