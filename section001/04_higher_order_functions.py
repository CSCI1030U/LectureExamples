# higher order functions 

def add_two(a, b):
    return a + b

def collapse_list(operation, list_of_numbers):
    total = list_of_numbers[0]

    for num in list_of_numbers[1:]:
        total = operation(total, num)

    return total

numbers = [1,2,3,4,5]
print(f'sum of {numbers} is {collapse_list(add_two, numbers)}')

def multiply_two(a, b):
    return a * b

numbers = [1,2,3,4,5]
print(f'product of {numbers} is {collapse_list(multiply_two, numbers)}')

numbers = [1,2,3,4,5,8,11,2,5,-1]
# def max_two(a, b):
#     # if a > b:
#     #     return a
#     # else:
#     #     return b
#     return a if a > b else b
# print(f'maximum of {numbers} is {collapse_list(max_two, numbers)}')
print(f'maximum of {numbers} is {collapse_list(lambda a,b: a if a > b else b, numbers)}')

# map

list_of_numbers = [1,2,3,4,5]
def times_two(x):
    return x * 2
list_of_doubles = list(map(times_two, list_of_numbers))
print(list_of_doubles)

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

list_of_ints = [123, 8765432, 17, 5, 0]
print(list(map(to_str, list_of_ints)))

# reduce
# from functools import reduce
from functools import reduce
print(f'maximum of {numbers} calculated with reduce() is {reduce(lambda a,b: a if a > b else b, numbers)}')

# filter

def b_range(mark):
    # if mark >= 70.0 and mark < 80.0:
    #     return True 
    # else:
    #     return False 
    return mark >= 70.0 and mark < 80.0

marks = [80.0, 75.0, 45.0, 71.5, 55.0, 90.0, 78.0]
print(list(filter(b_range, marks)))
print(list(filter(lambda mark: mark >= 70.0 and mark < 80.0, marks)))
