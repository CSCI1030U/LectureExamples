# coding challenge 1 (factorial)

'''
Math definition of factorial (!):

0! = 1
1! = 1
n! = n * (n - 1)!
'''

def factorial(n):
    if n == 0 or n == 1:
        return 1
    
    return n * factorial(n - 1)

print(f'{factorial(4) = }')
print(f'{factorial(5) = }')
print(f'{factorial(10) = }')

# coding challenge 2 (myfilter)

def myfilter(should_include, values):
    result_list = []

    for value in values:
        if should_include(value):
            result_list.append(value)

    return result_list

grades = [64.5, 87.0, 55.5, 94.0, 71.5, 46.0, 100.0]
print(f'{myfilter(lambda x: x > 80.0, grades) = }')
print(f'{myfilter(lambda x: x < 50.0, grades) = }')

# extra (recursive myfilter)

def myfilter_rec(should_include, values):
    if len(values) == 0:
        return []

    rest_results = myfilter_rec(should_include, values[1:])

    if should_include(values[0]):
        return [values[0]] + rest_results
    else:
        return rest_results

grades = [64.5, 87.0, 55.5, 94.0, 71.5, 46.0, 100.0]
print(f'{myfilter_rec(lambda x: x > 80.0, grades) = }')
