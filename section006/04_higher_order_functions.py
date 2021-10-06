# higher order functions 

# def add_two(a, b):
#     return a + b 

# exactly the same as reduce
def combine_list(combine_two, list_of_numbers):
    total = list_of_numbers[0]

    # for num in list_of_numbers[1:]:
    for index in range(1, len(list_of_numbers)):
        total = combine_two(total, list_of_numbers[index])  # calling our argument function

    return total

numbers = [1,2,3,4,5]
# print(f'The sum of {numbers} is {combine_list(add_two, numbers)}')
add_two = lambda a,b: a + b
print(f'The sum of {numbers} is {combine_list(add_two, numbers)}')

# def multiply_two(x, y):
#     return x * y

# print(f'The product of {numbers} is {combine_list(multiply_two, numbers)}')
print(f'The product of {numbers} is {combine_list(lambda a,b: a * b, numbers)}')

# map

def to_str(number):
    # go through each digit of the number (Hint: %)
    # add the string equivalent of the digit to a string
    string_rep = ''

    while number > 0:
        string_rep = str(number % 10) + string_rep  # 5
        number = number // 10 # 1234

    return string_rep

list_of_nums = [123, 876543, 0, 7, 11, 456]
list_of_string_reps = list(map(to_str, list_of_nums))

print(list_of_string_reps)

# reduce
from functools import reduce
print(f'The product of {numbers} (using reduce) is {reduce(lambda a,b: a * b, numbers)}')

print(reduce(lambda a,b: a if a > b else b, numbers))

# filter

def b_range(mark):
    # if mark >= 70.0 and mark < 80.0:
    #     return True 
    # else:
    #     return False 
    return mark >= 70.0 and mark < 80.0

marks = [44.5, 55.0, 62.5, 71.0, 66.5, 78.5, 95.0, 75.0]
# print(list(filter(b_range, marks)))
print(list(filter(lambda m: m >= 70.0 and m < 80.0, marks)))

# coding challenge

# def myfilter(f, values):
#     result_values = []

#     for val in values:
#         if f(val):
#             result_values.append(val)

#     return result_values

# recursive version, just for practice
def myfilter(f, values):
    # base step
    if len(values) == 0:
        return []

    # recursive step
    rest = myfilter(f, values[1:])  # filter the rest of the list
    if f(values[0]):
        rest = [values[0]] + rest
    
    return rest

print(list(myfilter(lambda m: m >= 70.0 and m < 80.0, marks)))


