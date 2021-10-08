# higher order functions, lambda expressions, map, reduce, filter

# our custom higher order function

def collapse_list(operation, list_of_numbers):
    total = list_of_numbers[0]

    for num in list_of_numbers[1:]:
        total = operation(total, num)
    
    return total

def add_two(a, b):
    return a + b

numbers = [1,2,3,4,5]

sum_of_list = collapse_list(add_two, numbers)
print(f'The sum of {numbers} is {sum_of_list}')

def multiply_two(a, b):
    return a * b

print(f'The product of {numbers} is {collapse_list(multiply_two, numbers)}')
print(f'The product of {numbers} is {collapse_list(lambda a,b: a * b, numbers)}')

numbers = [-13,8,4,-2,9,16,-9,-10,10]
print(f'The minimum of {numbers} is {collapse_list(lambda a,b: a if a < b else b, numbers)}')
print(f'The maximum of {numbers} is {collapse_list(lambda a,b: a if a > b else b, numbers)}')

# map - built-in higher order function

# def add_one(x):
#     return x + 1

numbers = [1,2,3,4,5]
print(list(map(lambda x: x + 1, numbers)))

def to_str(number):
    # go through each digit of the number (Hint: %)
    # add the string equivalent of the digit to a string
    string_rep = ''

    while number > 0:
        string_rep = str(number % 10) + string_rep  # 5
        number = number // 10 # 1234

    return string_rep

numbers = [123, 876543, 1, 17, 42]
print(list(map(to_str, numbers)))

# reduce - built-in higher order function

from functools import reduce
numbers = [-13,8,4,-2,9,16,-9,-10,10]
print(f'The minimum of {numbers} (reduce) is {reduce(lambda a,b: a if a < b else b, numbers)}')
print(f'The maximum of {numbers} (reduce) is {reduce(lambda a,b: a if a > b else b, numbers)}')

# filter - built-in higher order function

def b_range(mark):
    # if mark < 80.0 and mark >= 70.0:
    #     return True 
    # else:
    #     return False
    return mark < 80.0 and mark >= 70.0

marks = [100.0, 75.0, 55.0, 44.5, 65.5, 71.5, 78.0, 84.0, 91.0, 79.0]
print(f'The B grades in {marks} are {list(filter(b_range, marks))}')