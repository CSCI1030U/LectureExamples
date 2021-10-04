# functions (defining functions, arguments, return values, calling functions, pass by reference/value)

# named block of code that can be reused

def say_hello():
    print('Hello')

def get_message():
    # print('Greetings from Earth!')
    return 'Greetings from Earth!'

def get_important_value():
    return 42

def multiply(x, y):
    return x * y

def main():
    say_hello()

    print(say_hello)
    print(say_hello())

    msg = get_message()

    another_value = get_important_value() + 1

    product = multiply(3, 4)     # pass by value (copies the values)
    # print(x)     # out of scope

    a,b = 7,8
    product2 = multiply(a, b)    # copy the value of a into x, and copy the value of b into y

    print(f'The product of 3 and 4 is {product}')

    print(global_message)

global_message = 'this is a global variable'  # global variables are discouraged
main()


print('goodbye')

# coding challenge

# 123045 => '123045'

def to_str(number):
    # go through each digit of the number (Hint: %)
    # add the string equivalent of the digit to a string
    string_rep = ''

    while number > 0:
        string_rep = str(number % 10) + string_rep  # 5
        number = number // 10 # 1234

    return string_rep

n = 12345
print(f'The number {n} converted to a string is {to_str(n)}')