# Decimal: digits can be 0-9, e.g. 206, 000206 => 10
# Binary: digits can be 0 or 1, e.g. 1101 = 13 (decimal), 00001101

def to_binary(n, num_digits):
    result = ''

    digit_num = 0
    while (digit_num < num_digits):
        result = str(n % 2) + result
        n = n // 2

        digit_num += 1

    return result

print(to_binary(13, 8))

# 1100 1110
# 0 x 1   =   0
# 1 x 2   =   2
# 1 x 4   =   4
# 1 x 8   =   8
# 0 x 16  =   0
# 0 x 32  =   0
# 1 x 64  =  64
# 1 x 128 = 128

def print_n_times(n, message):
    # base case - otherwise we'd never exit!
    if n < 1:
        return

    print(f'{message} {n}')
    print_n_times(n - 1, message)

print_n_times(3, 'hello')

# 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# fib(0) = 0 
# fib(1) = 1
# fib(n) = fib(n - 1) + fib(n - 2)
def fib(n):
    # base case 
    if n <= 1:
        return n

    # recursive case
    return fib(n - 1) + fib(n - 2)

def fib_efficient(n):
    if n <= 1:
        return n

    last_fib = 1
    prev_fib = 0
    current_index = 1

    while current_index < n:
        current_fib = last_fib + prev_fib
        prev_fib = last_fib 
        last_fib = current_fib
        current_index += 1

    return last_fib

print(fib_efficient(0))
print(fib_efficient(1))
print(fib_efficient(2))
print(fib_efficient(3))
print(fib_efficient(4))
print(fib_efficient(5))
print(fib_efficient(100))
# 2^40 calls of fib()

def factorial(n):
    # base case
    if n <= 1:
        return 1

    # recursive case
    return n * factorial(n - 1)


# print(factorial(7)) # 5 * 4 * 3 * 2 * 1