# practice
def say_hello():
    print('Hello there!')

result = say_hello()
print(f'say_hello: {result = }')

def get_amazing_number():
    return 42

result = get_amazing_number()
print(f'get_amazing_number: {result = }')

def add_five(n):
    return n + 5

result = add_five(10)
print(f'add_five: {result = }')

def add(n, m):
    answer = n + m
    return answer

result = add(10, 12)
print(f'add: {result = }')

def infinite():
    print('Hello')
    infinite()

# infinite() # infinite recursion

def print_n_times(message, n):
    # for i in range(n):
    #     print(message)

    # base case (when to quit)
    if n <= 0:
        return

    # recursive case (when to keep going)
    print(message, n)
    print_n_times(message, n - 1)

print_n_times('Hello from recursion', 5)

# hackers' corner

add_also = lambda n, m: n + m
result = add_also(2, 4)
print(f'add_also: {result = }')

# coding exercise 4.1 (fibonacci)

'''
fib(0) = 0
fib(1) = 1
fib(n) = fib(n - 1) + fib(n - 2)
'''
def fib(n):
    if n == 0 or n == 1:
        return n

    return fib(n - 1) + fib(n - 2)

fib5 = fib(5)
print(f'{fib5 = }')

fib10 = fib(10)
print(f'{fib10 = }')

# coding challenge 1 (factorial)
'''
fact(0) = 1
fact(1) = 1
fact(n) = n * fact(n - 1)
'''

# higher order function examples

def double_it(num):
    return num * 2

def double_list(values):
    result = []

    for val in values:
        result.append(double_it(val))

    return result

def apply_op(values, operation):
    result_list = []

    for val in values:
        result = operation(val)
        result_list.append(result)

    return result_list

print(f'{apply_op([1,2,3], double_it) = }')

print(f'{apply_op([1,2,3], lambda num: num * 2) = }')
print(f'{apply_op([1,2,3], lambda num: num ** 2) = }')

# coding challenge 2 (myfilter)
