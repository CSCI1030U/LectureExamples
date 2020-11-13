import math 

# the famous divide and conquer algorithm - binary search
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

# traditional version (similar to divide and conquer)
def fibonacci(n):
    if n <= 1:
        return n 
    return fibonacci(n - 1) + fibonacci(n - 2)

# dynamic programming version of fibonacci
def better_fibonacci(n):
    solutions = [0, 1]
    if n < 2:
        return solutions[n]
    
    for i in range(2, n + 1):
        solutions.append(solutions[i - 1] + solutions[i - 2])
    
    return solutions[n]

print(better_fibonacci(100))
    

'''
                f(5)
        f(4)                f(3)
    f(3)    f(2)        f(2)    f(1)
'''

dictionary = [('Giselle Leclaire', 248.0), ('Fred Smith', 741.50)]
dictionary.append(('Roberta Juniper', 0.50))

key_to_find = 'Roberta Juniper'
for key,value in dictionary:
    if key == key_to_find:
        print(value)

# array[7] => array + (7 * size_of_int)
# ptr++ => ptr + size_of_int

# fractional knapsack problem
def fractionalKnapsack(items, capacity):
    # if there are no items, we cannot carry anything
    if len(items) < 1:
        return []

    # if we have no space, we cannot carry anything
    if capacity == 0:
        return []

    # choose the next best item (highest value)
    bestIndex = 0
    for i in range(len(items)):
        if items[i][1] > items[bestIndex][1]:
            bestIndex = i

    # determine how much of that item we can carry
    if capacity >= items[bestIndex][2]:
        # we can carry it all
        carry = items[bestIndex][0], items[bestIndex][2]
        capacity -= items[bestIndex][2]
        items = items[0:bestIndex] + items[bestIndex + 1:]
        return fractionalKnapsack(items, capacity) + [carry]
    else:
        # we can carry some, and fill our knapsack
        carry = items[bestIndex][0], capacity
        return [carry]

print('Knapsack:', fractionalKnapsack([('diamonds',11,8),('gold',5,13),('silver',3,6)], 20))
print('Knapsack:', fractionalKnapsack([('diamonds',11,8),('gold',5,13),('silver',3,6)], 25))
