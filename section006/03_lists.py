# lists (insertion, removal, len, max, min, in, index, count, 2D lists), list comprehension, tuples

student_names = ['Frida', 'Manpreet', 'Alex', 'Sam']

# inserting into a list
student_names.append('Barbara')  # result: ['Frida', 'Manpreet', 'Alex', 'Sam', 'Barbara']
student_names.insert(0, 'Fred') # result: ['Fred', 'Frida', 'Manpreet', 'Alex', 'Sam', 'Barbara']

# removing from a list 
student_names.remove('Fred') # result: ['Frida', 'Manpreet', 'Alex', 'Sam', 'Barbara']
student_names.pop(2)         # remove element at index 2, 'Alex', result: ['Frida', 'Manpreet', 'Sam', 'Barbara']

print(student_names)

print(min(student_names))
print(f'The maximum name is {max(student_names)}')
print(f'There are {len(student_names)} names in the list')

# for name in student_names:
#     print(name)

if 'Sam' in student_names:
    print('Yes, Sam is registered in this class')
else:
    print('No, Sam is not registered.')

print(f'Sam is at index {student_names.index("Sam")} inside the list')

if 'Carl' in student_names:
    print(f'Carl is at index {student_names.index("Carl")} inside the list')
else:
    print('Carl is not in the list')

student_names.append('Sam')

print(f'The name Jim appears {student_names.count("Jim")} times in the list')
print(f'The name Sam appears {student_names.count("Sam")} times in the list')

# *arrays* are provided by a library called NumPy
#   - array - contiguous values in order in memory

# 2D lists - lists of lists

gpu_prices = [
    [599.99, 899.99, 1199.99, 1499.99],  # september 2021
    [699.99, 999.99, 1349.99, 1599.99],  # august 2021
    [499.99, 799.99, 1099.99, 1349.99]   # july 2021
]

september_prices = [599.99, 899.99, 1199.99, 1499.99]
august_prices = [699.99, 999.99, 1349.99, 1599.99]
july_prices = [499.99, 799.99, 1099.99, 1349.99]

gpu_prices2 = [september_prices, august_prices, july_prices]

print(gpu_prices2)       # the whole list of lists
print(gpu_prices2[1])    # the second list within the list (august_prices)
print(gpu_prices2[1][2]) # the third element of the second list within the list (august_prices[2])

# list comprehensions

list1 = [1,2,3]
list2 = [x**2 for x in range(0, 10)]

# equivalent in math class:  { x^2 | x <- R, x >= 0, x < 10} (set)

list3 = []
for x in range(0, 10):
    list3.append(x**2)

print(f'The list comprehension results in {list2}')

# tuples (a sequence of values, usually different types)

x,y = 1,2

rtx3060 = 104, 'GeForce RTX 3060', '6 GB', 'RJF Electronics', 499.99, [271, 340]
rtx3070 = 105, 'GeForce RTX 3070', '8 GB', 'RJF Electronics', 599.99, [271, 340]
rtx3080 = (106, 'GeForce RTX 3080', '10 GB', 'RJF Electronics', 699.99, [271, 340])
rtx3090 = 107, 'GeForce RTX 3090', '12 GB', 'RJF Electronics', 799.99, [271, 340]

PRICE = 4

# list of tuples
gpus = [
    (104, 'GeForce RTX 3060',  '6 GB', 'RJF Electronics', 499.99, [271, 340]),
    (105, 'GeForce RTX 3070',  '8 GB', 'RJF Electronics', 599.99, [271, 340]),
    (106, 'GeForce RTX 3080', '10 GB', 'RJF Electronics', 699.99, [271, 340]),
    (107, 'GeForce RTX 3090', '12 GB', 'RJF Electronics', 799.99, [271, 340])
]

print(f'The price of the 3090 is ${rtx3090[PRICE]}')
print(rtx3090)

# this syntax is from a dictionary
# rtx3090.price

# advantages of functions:
#
# 1. unit for dividing up your code (cognitive capacity - 5-9)
# 2. names a snippet of code (readable)
# 3. duplicated code is reduced (errors aren't going to be duplicated)
# 4. can individual test each function (unit testing)
