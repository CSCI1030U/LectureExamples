# practice

our_type = 'Fire'
enemy_type = 'Fire'

our_damage = 30

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

for x in [0,1,2,3,4,5,6,7,8,9]:
    print(f'for loop (list) {x}')

for n in range(10): # range(0, 10, 1)
    print(f'for loop (range) {n}')

for i in range(17, 5, -3):
    print(f'for loop (by threes) {i}')

# hacker's corner

m,n = -6,-1

if m > n:
    max2 = m 
else:
    max2 = n

# unary   (e.g. -7, not is_on)
# binary  (e.g. 2 + 3, is_on and has_battery)
# ternary (e.g. val1 if condition else val2)

max2 = m if m > n else n

print(f'{max2 = }')

# { x | x < 4 }
gen1 = (x ** 2 + 1 for x in [1,2,3])
for i in gen1:
    print(f'gen1: {i}')

gen2 = (n * 3 + 4 for n in range(0, 10, 2))
for i in gen2:
    print(f'gen2: {i}')

# coding exercise

import math

x = 1
num_terms = 20
e_estimate = 0.0

for n in range(num_terms):
    numerator = x ** n
    denominator = math.factorial(n)
    e_estimate += numerator / denominator

    print(f'{e_estimate=}')