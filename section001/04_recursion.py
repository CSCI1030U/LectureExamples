# recursive functions, infinite recursion, tail recursion

# tail recursion - recursive call is the very last step

# infinite recursion
# also tail recursive
def forever():
    print('hello')
    forever()

# equivalent iterative code:
# while True:
#     print('hello')

# forever()

# def print_n_times(n, message):
#     for x in range(n):
#         print(message)

# tail recursive
def print_n_times(n, message):
    # base step
    # should we exit?

    if n <= 0:
        return
    
    print(f'{n} {message}')

    # recursive step
    print_n_times(n - 1, message)

print_n_times(3, 'Hello world!')

# coding exercise - fibonacci

# fibonacci:  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

# Fib n =     n, if n == 0 or n == 1
#             Fib(n-1) + Fib(n-2), if n > 1

# Note:  This is very inefficient, but simple and elegant

# not tail recursive

def fib(n):
    if n == 0 or n == 1:
        return n
    
    return fib(n - 1) + fib(n - 2)

x = 8
print(f'The {x}th fibonacci number is {fib(x)}')

# coding challenge

# factorial(1) = 1
# factorial(n) = n * factorial(n - 1)