import math 

name = 'Randy'

math.factorial(5)

# single responsibility principle - a function should just do one thing
def factorial(n):
    # factorial(5) = 5 * 4 * 3 * 2 * 1 = 1 * 2 * 3 * 4 * 5
    # print(name) # yuck!  accessing global vars inside a function is a bad practice
    # name = 'Joseph'
    
    result = 1
    for multiplier in range(1, n + 1):
        result *= multiplier

    return result

print('factorial of 5 is', factorial(5))
print('factorial of 6 is', factorial(6))
# print(f'result = {result}')
print(name)
