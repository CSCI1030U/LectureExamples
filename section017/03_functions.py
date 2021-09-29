# functions (defining functions, arguments, return values, calling functions, pass by reference/value)

# reusable, named blocks of code

def say_hello():
    print('Hello')

def get_the_answer():
    # print(42)
    return 42 # not the same as printing

def multiply(a, b):
    return a * b

def main():
    say_hello() # calling our function
    say_hello()

    the_ultimate_answer = get_the_answer()

    # call by value (values are copied into the argument variables)
    product_of_3_and_4 = multiply(3, 4)

    print(product_of_3_and_4)  # product_of_3_and_4 is local to main()
    # print(a)                   # a is local to multiply(), out of scope here

main()

print(say_hello())
print(say_hello)
print(get_the_answer())

# coding challenge 

# 12345 => '12345'

def to_str(number):
    # YOUR CODE GOES HERE

    # Go digit by digit through the number (Hint: %)
    # Add the corresponding character for that digit to the string

print(to_str(12345))