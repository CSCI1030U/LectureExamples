# coding challenge - sin of x

num_iterations = 10
x = 3 * math.pi / 2
n = 0
total = 0
while n < num_iterations:
    sign = (-1) ** n
    exponent = x ** (2 * n + 1)
    factorial = math.factorial(2 * n + 1)
    total += sign * exponent / factorial
    n += 1

print(f'sin(x): {total = }')

# coding exercise 2 - square root using the bisection method

x = 2

lower = 0.0
upper = x
guess = (lower + upper) / 2
while abs(guess ** 2 - x) >= 0.00000000001:
    print(f'  guess = {guess}')
    if guess ** 2 < x:
        # our guess is too low
        lower = guess
    elif guess ** 2 > x:
        # our guess is too high
        upper = guess

    guess = (lower + upper) / 2

print(f'The square root of {x} is {guess}')
