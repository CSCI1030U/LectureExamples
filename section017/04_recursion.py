# recursive functions, infinite recursion, tail recursion

def print_nums(start, stop):
    if start == stop:
        return

    print(start, end=' ')
    print_nums(start + 1, stop)

def forever():
    print('hello')
    forever()

# the recursive call below is similar to this for loop
# for x in range(0, 10):
#     print(x)

# forever()  # infinite recursion
print_nums(0, 10)

def repeat_n_times(n, message):
    # exit when n is small enough
    if n <= 0:
        return

    print(message)
    # tail recursion - recursive step
    repeat_n_times(n - 1, message)

print('')
repeat_n_times(5, 'hello there')

# coding exercise

# Note:  This is very inefficient

# fibonacci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
def fibonacci(n):
    # base case
    if n <= 1:    
        return n

    # recursive case (not tail recursive)
    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_efficient(n):
    index = 1
    last_num = 1
    second_last = 0
    while index < n:
        current = last_num + second_last
        index += 1

        second_last = last_num
        last_num = current
    return current

x = 60
print(f'The {x}th fibonacci number is {fibonacci_efficient(x)}')

# coding challenge (write a recursive factorial function)

# factorial(n) => n * (n-1) * (n-2) * (n-3) * ... * 3 * 2 * 1
def factorial_loop(n):
   result = 1
   for i in range(1, n+1):
      result = result * i
   return result

x = 5
print(f'{x} factorial is equal to {factorial_loop(x)}')


# factorial(n) = 1, if n == 1
#              = n * factorial(n - 1), otherwise
def factorial_recursion(n):
    if n <= 0:
        return f'Error: factorial not defined for {n}'

    if n == 1:
        return 1
    
    return n * factorial_recursion(n - 1) # not tail recursive

x = 5
print(f'{x}! is equal to {factorial_recursion(x)}')

# converting from tail recursive to iterative

# def print_n_times(n, message):
#    if n == 0:
#       return
#    print(message)
#    print_n_times(n - 1, message)

def print_n_times(n, message):
    while n > 0:
        print(message)
        n = n - 1

print_n_times(5, 'Hello')
