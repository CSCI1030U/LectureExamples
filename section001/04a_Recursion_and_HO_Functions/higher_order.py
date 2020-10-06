def traverse(values, function):
    for val in values:
        function(val)

def scale_and_print(grade):
    print(grade / 10.0)

assignment_grades = [85.0, 95.0, 100.0, 60.0, 85.0, 90.0, 80.0, 55.0]
# traverse(assignment_grades, scale_and_print)

def print_if_odd(val):
    if val % 2 == 1:
        print(val, 'is an odd number.')

values = [1,2,3,4,5,6,7,8,9,10]
traverse(values, print_if_odd)

# def farenheit_to_celcius(freedom):
#     return (freedom - 32) * 5 / 9

f_temps = [40.0, 50.0, 60.0, 70.0, 80.0, 90.0]
# c_temps = list(map(farenheit_to_celcius, f_temps))
c_temps = list(map(lambda f: (f - 32) * 5 / 9, f_temps))
print(c_temps)

from functools import reduce

marks = [9.5, 10.0, 8.0, 32.5, 28.0]
final_mark = reduce(lambda a,b: a + b, marks)
print(final_mark)

n = 6
result = reduce(lambda x,y: x * y, range(1, n + 1))
print(result)

names = ['Randy', 'Suzie-Jane', 'Ricardo', 'Kumar', 'Alicia', 'Eduardo', 'Rick', 'Randy the 2nd', 'Muhammad']
def is_long(name):
    # if len(name) >= 7:
    #     return True
    # else:
    #     return False 
    return len(name) >= 7
long_names = list(myfilter(is_long, names))
print(long_names)

