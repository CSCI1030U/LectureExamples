import math 

def binary_search(x, a, start, end):
    if start > end:
        return False 
    
    middle_index = (start + end) // 2

    if x == a[middle_index]:
        return True 
    elif x < a[middle_index]:
        return binary_search(x, a, start, middle_index - 1)
    else: # x > a[middle_index]
        return binary_search(x, a, middle_index + 1, end)

values = [0,2,4,6,8,10,12,14,16,18,20]
print(binary_search(2, values, 0, len(values) - 1))