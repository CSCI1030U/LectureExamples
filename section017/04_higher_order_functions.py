# higher order functions 

def combine_list(list_of_nums, operation):
    total = list_of_nums[0]  # first element is the start value
    for index in range(1, len(list_of_nums)):
        total = operation(total, list_of_nums[index])
    return total 

# def add_two(a, b):
#     return a + b

add_two = lambda a,b: a + b

numbers = [1,2,3,4,5]
sum_of_numbers = combine_list(numbers, add_two)
product_of_numbers = combine_list(numbers, lambda a,b: a * b)

print(f'sum_of_numbers == {sum_of_numbers}')
print(f'product_of_numbers == {product_of_numbers}')

# map

def to_str(number): # from an earlier lecture
    # Go digit by digit through the number (Hint: %)
    # Add the corresponding character for that digit to the string
    if number == 0:
        return '0'

    string_rep = ''

    while number > 0:
        string_rep = str(number % 10) + string_rep   # right-most digit
        number = number // 10 # remaining digits
        # print(f'number = {number}')

    return string_rep

numbers = [123, 456, 1, 0, 17, 45000]
list_of_string_reps = list(map(to_str, numbers))
print(list_of_string_reps)

# reduce
from functools import reduce

multiply_two = lambda u,v: u * v
product_of_numbers = reduce(multiply_two, [1,2,3,4,5])

print(f'product_of_numbers (reduce) == {product_of_numbers}')

# filter

def b_range(grade):
    # if grade < 80.0 and grade >= 70.0:
    #     return True 
    # else:
    #     return False
    return grade < 80.0 and grade >= 70.0

grades = [50.0, 45.0, 66.5, 82.0, 78.0, 55.25, 87.5, 100.0, 74.5, 50.0, 94.5]
print(f'The B range grades are {list(filter(b_range, grades))}')

# coding challenge

# def myfilter(include_check, values):
#     result_values = []
#     for val in values:
#         if include_check(val):
#             result_values.append(val)
#     return result_values

# recursive version (for extra practice)
def myfilter(include_check, values):
    # base step
    if len(values) == 0:
        return []

    # recursive step
    if include_check(values[0]):
        return [values[0]] + myfilter(include_check, values[1:])
    else:
        return myfilter(include_check, values[1:])

print(f'B range grades in {grades} are {list(myfilter(b_range, grades))}')
