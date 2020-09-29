# n = 12345
# output: '12345'

def int_to_str(num):
    digits = '0123456789'

    result = ''

    while num > 0:
        d = num % 10
        result = digits[d] + result
        num = num // 10

    return result

print(int_to_str(-12345678))
print(str(12345678))

# def forever():
#     print('hello')
#     forever()

# forever()

def print_n_times(n, message):
    # base case
    if n == 0:
        return

    print(message)

    # recursive case
    print_n_times(n - 1, message)

print_n_times(3, 'Hello world!')

# 0, 1, 1, 2, 3, 5, 8, ...
# fibonacci(0) = 0
# fibonacci(1) = 1
# fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(0))
# print(fibonacci(1))
# print(fibonacci(2))
# print(fibonacci(3))
# print(fibonacci(4))
# print(fibonacci(5))
print(fibonacci(50))

'''
The adventurous might want to try to implement this sequence (using a loop, most likely):

the hailstone sequence:
- If n is 1 then the sequence ends.
- If n is even then the next n of the sequence = n/2.
- If n is odd then the next n of the sequence = (3 * n) + 1.
'''