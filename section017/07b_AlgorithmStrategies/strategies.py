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