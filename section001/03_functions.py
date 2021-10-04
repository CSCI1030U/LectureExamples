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

# modulo operator (%) review:
#   8765432 % 10 => 2
#   0 % 10 => 0

# 12345 => '12345'
def to_str(number):
    # go through the number one digit at a time (Hint: %)
    # add each digit's character to the string
    string_rep = ''

    # number = 12345
    # string_rep = ''

    # iteration 1
    # string_rep = '' + '5' => '5'
    # number = 1234

    # iteration 2
    # string_rep = '5' + '4' => '54'
    # number = 123

    # iteration 3
    # string_rep = '54' + '3' => '543'
    # number = 12

    # iteration 4
    # string_rep = '543' + '2' => '5432'
    # number = 1

    # iteration 5
    # string_rep = '5432' + '1' + '54321'
    # number = 0

    while number > 0:
        string_rep = str(number % 10) + string_rep 

        number = number // 10 # floor division

    return string_rep

print(to_str(12345))
