age_string = input('Enter your age: ')
age = int(age_string)

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
x = 8.0
epsilon = 0.05

low = 0.0
high = x

guess = (low + high) / 2

while abs(guess**2 - x) >= epsilon:
    print(f'low = {low}, high = {high}, guess={guess}')

    if (guess**2 - x) < 0:
        # increase our guess