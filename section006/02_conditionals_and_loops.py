# practice

our_type = 'Fire'
enemy_type = 'Grass'

if our_type == 'Fire' and enemy_type == 'Water':
    move_strength_factor = 0.5
elif our_type == 'Fire' and enemy_type == 'Fire':
    move_strength_factor = 0.5
elif our_type == 'Fire' and enemy_type == 'Grass':
    move_strength_factor = 2.0

print(f'Our pokemon does {30 * move_strength_factor} damage.')

n = 0
while n < 10:
    print(f'While loop: {n}')
    n += 1

for n in [0,1,2,3,4,5,6,7,8,9]:
    print(f'For loop (list): {n}')

for n in range(10): # range(0, 10, 1)
    print(f'For loop (range): {n}')

# hacker's corner

a,b = 1,2
if b > a:
    max2 = b
else:
    max2 = a

# unary (-7)
# binary (2 + 1)
# ternary 

max2 = a if a > b else b

gen1 = (2 * n for n in [1,2,3])
for i in gen1:
    print(f'gen1 output: {i = }')

gen2 = (n ** 2 for n in range(5,15,3))
for i in gen2:
    print(f'gen2 output: {i = }')

# coding exercise (e ** x)

import math 

num_iterations = 10
x = 1
estimate = 0.0
for n in range(num_iterations):
    numer = (x ** n)
    denom = math.factorial(n)
    estimate += numer / denom

print(f'Estimate for e**x: {estimate}')
