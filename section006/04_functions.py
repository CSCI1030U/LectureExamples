# practice
def say_hello():
    print('Hello!')
    return # optional

say_hello_result = say_hello()
print(f'{say_hello_result = }')

def get_the_answer():
    return 42

    print('This won\'t happen')

get_the_answer_result = get_the_answer()
print(f'{get_the_answer = }')
print(f'{get_the_answer_result = }')

def multiply(a, b):
    prod = a * b
    print(f'{prod = }')
    return prod

product = multiply(3, 4)
print(f'{product = }')

def infinite():
    print('Hello again!')
    infinite()

# infinite()

def print_n_times(n, message):
    # base case
    if n == 0:
        return

    # recursive case 
    print(message)
    print_n_times(n - 1, message)

print_n_times(10, 'Hello there')

# coding exercise (fibonacci)

def fib(n):
    # base case
    if n == 0 or n == 1:
        return n

    # recursive case
    return fib(n - 1) + fib(n - 2)

# 0, 1, 1, 2, 3, 5, 8, 13, ...
print(f'{fib(0) = }')
print(f'{fib(1) = }')
print(f'{fib(2) = }')
print(f'{fib(3) = }')
print(f'{fib(4) = }')
print(f'{fib(5) = }')
print(f'{fib(6) = }')
# print(f'{fib(50) = }')

def traverse(elements, operation):
    for elem in elements:
        operation(elem)

traverse(['Randy', 'Joseph', 'Fortier'], print)

# hackers' corner (lambda expressions)

f_temps = [50.0, 60.0, 70.0, 80.0, 90.0, 100.0]

def far_to_cel(farenheit):
    return (farenheit - 32) * 5 / 9

c_temps = map(far_to_cel, f_temps)
print(f'{list(c_temps) = }')

c_temps = map(lambda f: (f - 32) * 5 / 9, f_temps)

