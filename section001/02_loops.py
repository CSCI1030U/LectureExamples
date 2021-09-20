# 02 - loops

# x = 0
# while x < 100:
#     print(f'{x} is small')
#     x += 1

# for x in [0,1,2,3,4,5,6,7,8,9]
for x in range(16, 0, -4):  # start, stop, step
    print(f'{x} is small')

# estimate for pi
pi_estimate = 0.0
for n in range(1, 1000001):
    term = -1 * (-1)**n / (2 * n - 1)
    # print(f'term == {term}')
    pi_estimate += term

pi_estimate *= 4.0
print(f'Estimated value for pi: {pi_estimate}')

# infinite loop
# x = 0
# while x < 10:
#     # print(x, 'is small')
#     x = x - 1

# coding exercise - square root

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