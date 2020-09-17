# age_string = input('Enter your age: ')
#age = int(age_string)
age = 10

if (age <= 10) and (age >= 5):
    print('Teletubbies')
else:
    print('Breaking Bad')

if 5 < age < 10:
    print('Between 5 and 10')
    print('Another print')

print('Your age is', age)
print(f'Your age is {age}')

if age <= 2:
    print('Hold my hand')
elif age <= 5:
    print('Wait for me')
elif age <= 12:
    print('Not tonight!')
else:
    print('Go for it')

print('while loop:')
x = 0
while x < 10:
    print(x)
    x += 1

print('for loop 1:')
for y in [0,1,2,3]:
    print(y)

print('for loop 2:')
for y in range(10, 25, 5):
    print(y)

print('for loop 3:')
for y in range(100, 50, -15):
    print(y)

print('for loop 4:')
for y in range(3):
    print('hello')

# coding exercise
x = 13.0
epsilon = 0.01

low = 0.0
high = x

guess = (low + high) / 2.0
num_guesses = 0

while abs(guess**2 - x) >= epsilon:
    num_guesses += 1
    print(f'low = {low}, high = {high}, guess={guess}, guess squared:', guess**2)

    if guess**2 == x:
        # we guessed it!
        print('Yay')
    elif guess**2 < x:
        # increase our guess (our guess is too low)
        low = guess
    else:
        # decrease our guess (our guess is too high)
        high = guess 

    guess = (low + high) / 2.0

# coding exercise 2

# sin(x) = x**1 / 1! - x**3 / 3! + x**5 / 5! - x**7 / 7! + x**9 / 9! - x**11 / 11! + ...
# e**x = x**0/0! + x**1/1! + x**2/2! + x**3/e! + x**4/4! + x**5/5! + ...

import math

x = 1.0
estimate = 0.0
number_of_terms = 100
for n in range(0, number_of_terms, 1):
    term = x ** n / math.factorial(n)
    estimate += term

print(f'estimate = {estimate}, actual value = {math.e}')

# 8 / 2 == 4
# 9 / 2 == 4.5
# 9 // 2 == 4
# 9 % 2 == 1   (modulo)

num = 32
if (num % 2) == 0:
    print(f'{num} is an even number')
else:
    print(f'{num} is an odd number')
