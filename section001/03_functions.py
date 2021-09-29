# functions (defining functions, arguments, return values, calling functions, pass by reference/value)

def say_hello():
    print('Hello')

def get_amazing_number():
    return 42

def multiply(a, b):
    return a * b

def print_list(names):
    print(names)

def main():
    say_hello()
    say_hello()

    amazing_number = get_amazing_number() + 1
    print(f'The amazing number is {amazing_number}')

    print(say_hello())

    result = multiply(3, 4)   # pass by value (copies the value of 3 into the variable a, and it copies 4 into the variable b)
    print(f'3 multiplied by 4 is {result}')

    x = 5
    y = 8
    result2 = multiply(x, y)  # also pass by value

    student_names = ['Barbara', 'Manpreet']
    print_list(student_names) # pass by reference

    print(test_marks)

test_marks = [10.0, 20.0, 15.5, 14.25] # discouraged to use global variables
x = 3

main()


# coding challenge

# 12345 => '12345'
def to_str(number):
    # YOUR CODE GOES HERE

    # go through the number one digit at a time (Hint: %)
    # add each digit's character to the string

