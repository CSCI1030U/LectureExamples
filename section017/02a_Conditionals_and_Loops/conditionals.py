
age = 18
# print(age < 12)
if age < 12:
    print('Vote, what is that?')
elif age < 18:
    # age is between 12 and 18 (including 12)
    print('It is important to vote!')
elif age > 80:
    # age > 80 only
    print('It is important to vote!')
else:
    print('Get out there and vote right now!')

x = 0
while x < 10:
    print(x)
    x += 1

print('for loop:')
grades = [1,2,3,4,5]
for g in grades:
    print(g)

print('while loop:')
index = 0
while index < 5:
    print(grades[index])
    index += 1

print('for loop 2:')
# range(5) => [0,1,2,3,4]
# start, stop, step
for x in range(20, 10, -2):
    print(x)

# coding exercise
x = 8.0

low = 0
high = x 

guess = (low + high) / 2.0

epsilon = 0.000000000001

while abs(guess**2 - x) >= epsilon:

    # modify low and/or high to narrow the guess

    # if our guess is too big, then use 'guess' as the new 'high'
    if guess**2 - x > 0:
        high = guess

    # if our guess is too small, the use 'guess' as the new 'low'
    if guess**2 - x < 0:
        low = guess

    guess = (low + high) / 2.0

import math

print(f'guess: {guess}')
print('real: ', math.sqrt(8.0))

# coding exercise #2

# e**x = x**0/0! + x**1/1! + x**2/2! + x**3/3! + x**4/4! + ...
# Notes:
#   x = x**1/1!
#   1 = x**0/0!
#   0! = 1

x = 1.0
total = 0.0

for n in range(100):
    term = x**n / math.factorial(n)
    total += term

print(f'e**x approximated is {total}')
