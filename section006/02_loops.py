# 02 - loops

# x = 0
# while x < 5:
#     print('Hello')
#     x += 1

# for x in range(5):  # range(start, stop, step)
#     print(x)

for x in range(10, 30, -2):
    print(x)

pi_estimate = 0.0
for n in range(1, 100000):
    term = (-1)**n / (2 * n - 1)
    pi_estimate += term 

pi_estimate *= -4
print(f'An estimate for pi: {pi_estimate}')

# infinite loop:
# x = 0
# while x < 10:
#     print('hello')

x = 2.0

lower = 0.0
upper = x

guess = (lower + upper) / 2.0

while abs(guess**2 - x) >= 0.0000000001:
    print(f'  guess = {guess}')
    if guess**2 < x:
        # narrow down our guess (too low)
        lower = guess
    elif guess**2 > x:
        # narrow down our guess (too high)
        upper = guess
    guess = (lower + upper) / 2
print(f'guess = {guess}')