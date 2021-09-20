# 02 - loops

# x = 0
# while x < 10:
#     print(x)
#     x += 1

for x in range(3):
    print('Hello!')

# x = 0
# while x < 3:
#     print('Hello')
#     x += 1

x = 1
while x < 1000000:
    x *= 1.1
print(x)


# range(10) => [0,1,2,3,4,5,6,7,8,9]  (in older versions of Python)

natural_log_of_2 = 0
for n in range(1, 100001):
    term = (-1)**n / n
    natural_log_of_2 += term
natural_log_of_2 *= -1
print(f'natural log of 2: {natural_log_of_2}')

pi_estimate = 0
n = 1
while n < 100000:
    term = (-1)**n / (2 * n - 1)
    pi_estimate += term 
    n += 1
pi_estimate *= -4
print(f'estimate for pi: {pi_estimate}')

# coding exercise

x = 9.0

low = 0.0
high = x 

guess = (low + high) / 2

while abs(guess**2 - x) >= 0.00000001:
    # check if the answer is correct
    if guess**2 == x:
        print(f'The square root of {x} is {guess}')
        break

    elif guess**2 < x:
        # too low
        low = guess

    elif guess**2 > x:
        # too high
        high = guess 
    
    guess = (low + high) / 2

print(f'The square root of {x} is {guess}')