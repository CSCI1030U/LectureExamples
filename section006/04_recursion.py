# recursive functions, infinite recursion, tail recursion

# tail recursion - the recursive call comes *last*

# infinite recursion
# tail recursion
def forever():
    print('hello')
    forever()

# forever()

# tail recursive
def print_n_times(n, message):
    # base step (check if you need to exit)
    if n <= 0:
        return

    print(f'{n} {message}')

    # recursive step
    print_n_times(n - 1, message)

# converted to an iterative version:
# def print_n_times(n, message):
#     while n > 0:
#         print(f'{n} {message}')
#         n = n - 1


print_n_times(2, 'This is the message')

# fibonacci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

# Note: This is very inefficient, but very simple/elegant
# not tail recursion, since the + happens last
def fibonacci_rec(n):
    if n == 0 or n == 1:
        return n 
    
    return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)

x = 10
print(f'The {x}th fibonacci number is {fibonacci_rec(x)}')

# coding challenge

# n! = n * (n-1) * (n-2) * (n-3) * ... * 3 * 2 * 1

# recursive definition of factorial:
#
# n! = 1, if n == 1
#    = n * (n-1)!, for n > 1

def factorial_loop(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

x = 5
print(f'{x}! is equal to {factorial_loop(x)}')

# not tail recursive since * happens last
def factorial_rec(n):
    if n == 1:
        return 1

    return n * factorial_rec(n - 1)

x = 5
print(f'{x}! is equal to {factorial_rec(x)}')