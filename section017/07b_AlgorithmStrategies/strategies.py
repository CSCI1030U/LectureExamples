import math 

math.ceil(3.1) # => 4
math.floor(3.9) # => 3

def binary_search(x, a, start, end):
    # the list is empty, so we didn't find the element
    if start > end:
        return False

    # find the middle index
    middle_index = (start + end) // 2

    if x == a[middle_index]:
        # yay, we found it!
        return True 
    elif x < a[middle_index]:
        # search the left half of the list, recursively
        return binary_search(x, a, start, middle_index - 1)
    else:  # x > a[middle_index]
        # search the right half of the list, recursively
        return binary_search(x, a, middle_index + 1, end)

values = [-8, -2, 0, 3, 5, 10, 22, 24]
print(binary_search(2, values, 0, len(values) - 1))

def terrible_fibonacci(n):
    if n <= 1:
        return n 
    
    return terrible_fibonacci(n - 1) + terrible_fibonacci(n - 2)

def better_fibonacci(n):
    solutions = [0, 1]
    if n <= 1:
        return solutions[n]
    
    for i in range(2, n + 1):
        solutions.append(solutions[i - 1] + solutions[i - 2])
    
    return solutions[n]

print(better_fibonacci(100))

marks_dictionary = [('100000001', 67.5), ('100000002', 70.0)]
marks_dictionary.append(('100000003', 75.5))
print(marks_dictionary)

sid_to_find = '100000003'
for sid, mark in marks_dictionary:
    if sid == sid_to_find:
        print(mark)

'''
float[] marks = ...;
cout << marks[3];

marks + (3 * size_of_int)
'''
