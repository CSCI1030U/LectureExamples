# practice

age = 8
if age < 5:
    print('You are too young for pokemon')
elif age < 40:
    print('Pokemon is for kids, so enjoy!')
else:
    print('You are too old for pokemon, sorry!')

n = 0
while n < 10:
    print(f'Print (while loop) {n}')
    n += 1

for n in [0,1,2,3,4,5,6,7,8,9]:
    print(f'Print (for loop with list) {n}')

for n in range(10): # range(0, 10, 1):
    print(f'Print (for loop with range) {n}')

for n in range(9, -1, -1):
    print(f'Print (backwards loop) {n}')

# hacker's corner

# unary:   -7
# binary:  2 - 3
# ternary: question ? answer1 : answer2 (C++)
#          answer1 if question else answer2 (Python)

# ternary operator
message = 'You can like Pokemon!' if age < 40 else 'You are too old for Pokemon'

gen1 = (n**2 for n in [1,2,3,4,5])
print(f'{list(gen1) = }')

gen2 = (n for n in range(5, 15, 3))
for i in gen2:
    print(f'{i = }')

# a real exercise

pi_estimate = 0.0
for n in range(1, 1000001):
    term = -1 * (-1)**n / (2 * n - 1)
    pi_estimate += term

print(f'{pi_estimate*4 = }')

# coding exercise 2.1

import math

x = 1
num_iterations = 10
total = 0.0

for n in range(num_iterations):
    numerator = x ** n
    denominator = math.factorial(n)
    total += numerator / denominator

print(f'Estimate for e**1: {total = }')
