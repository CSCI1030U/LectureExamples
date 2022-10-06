# practice
def say_hello():
    print('Hello there!')
    return # not necessary

say_hello_result = say_hello()
print(f'{say_hello_result = }')

def get_the_answer():
    return 42

answer_result = get_the_answer()
print(f'{answer_result = }')
print(f'{get_the_answer = }')

def multiply(a, b):
    prod = a * b
    print(f'{prod = }')
    return prod

product = multiply(3, 4)
print(f'{product = }')

def infinite():
    print('Hello there!')
    infinite()

# infinite()

def print_n_times(n, message):
    # base case 
    if n == 0:
        return

    # recursive case
    print(message)
    print_n_times(n - 1, message)

print_n_times(10, 'Hello again!')

# coding exercise (fibonacci)

def fib(n):
    # base case
    if n == 0 or n == 1:
        return n

    # recursive case
    return fib(n - 1) + fib(n - 2)

print(f'{fib(0) = }')
print(f'{fib(1) = }')
print(f'{fib(2) = }')
print(f'{fib(3) = }')
print(f'{fib(4) = }')
print(f'{fib(5) = }')
print(f'{fib(6) = }')
# print(f'{fib(50) = }')


# hackers' corner

def traverse(elements, operation):
    for elem in elements:
        operation(elem)

traverse(['Randy', 'Joseph', 'Fortier'], print)
