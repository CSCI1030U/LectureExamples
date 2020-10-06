def print_score(mark):
    print(mark / 10.0)

def traverse(values, function):
    for val in values:
        function(val)

assignment_marks = [100.0, 95.0, 70.0, 55.0, 95.0, 100.0]
# traverse(assignment_marks, print_score)

names = ['Lebron', 'Coby', 'Bob', 'Katy', 'Emily', 'Shaquilla', 'Canada', 'Mia']
def say_hi(name):
    print(f'Hello, {name}!')
# traverse(names, say_hi)

def farenheit_to_celcius(farenheit):
    return (farenheit - 32) * 5 / 9

f_temps = [-10.0, 0.0, 10.0, 20.0, 90.0]
c_temps = list(map(farenheit_to_celcius, f_temps))
print(c_temps)

f_temps = [-10.0, 0.0, 10.0, 20.0, 90.0]
c_temps = list(map(lambda f: (f - 32) * 5/9, f_temps))
print(c_temps)

from functools import reduce 

def concat(a, b):
    return a + b 
words = ['the', 'quick', 'brown', 'fox', 'jumps']
result = reduce(concat, words)
print(result)

print(reduce(lambda a,b: a + b, words))

names = ['Lebron', 'Coby', 'Bob', 'Katy', 'Emily', 'Shaquilla', 'Canada', 'Mia']

def myfilter(function, values):
    # build a list from values
    #  1. initially empty
    #  2. check every value
    #     2a. call the function
    #     2b. if True, then add the value to the list
    #  3. return the list

    result = []

    for val in values:
        if function(val):
            result.append(val)

    return result

def is_short(name):
    # if len(name) < 5:
    #     return True 
    # else:
    #     return False 
    return len(name) < 5
short_names = list(myfilter(is_short, names))
print(short_names)