# lists (insertion, removal, len, max, min, in, index, count, 2D lists), list comprehension, tuples

student_names = ['Frida', 'Manpreet', 'Alex', 'Sam']
student_names.append('Robert')  # adds to the end
# result:  ['Frida', 'Manpreet', 'Alex', 'Sam', 'Robert']

student_names.insert(0, 'Becky')
# result:  ['Becky', 'Frida', 'Manpreet', 'Alex', 'Sam', 'Robert']

student_names.remove('Alex')

print(student_names[0])
print(len(student_names[0]))

student_names[0] = 'Rebecca'
print(student_names[0])

test_marks = [80.0, 72.5, 60.0, 42.0, 75.5, 55.25]
print(f'the highest grade was {max(test_marks)}.')
lowest_mark = min(test_marks)
print(f'the lowest mark was {lowest_mark}.')

# Python has arrays - in a library called NumPy
print(f'the max student name? is {max(student_names)}')  # alphabetical

if 'Sam' in student_names:   # also available: 'not in'
    print('Yes, Sam is registered')
else:
    print('No, Sam is not in your class')

print(student_names.index('Sam'))
# print(student_names.index('Barbara'))  # runtime error

student_names.append('Sam')
print(student_names)
print(student_names.count('Sam'))

# list comprehensions

list1 = [x**2 for x in range(0, 100)]
print(list1)

# tuple - another sequence, can contain different types

part1 = 101, 'GeForce RTX 3070', '6 GB', 899.99
part2 = 102, 'GeForce RTX 3080', '10 GB', 1299.99

# for field in part:
#     print(field)

# list of tuples
gpus = [part1, part2, (103, 'GeForce RTX 3090', '12 GB', 1899.99)]

gpus2 = [
    (101, 'GeForce RTX 3070', '6 GB', 899.99),
    (102, 'GeForce RTX 3080', '10 GB', 1299.99),
    (103, 'GeForce RTX 3090', '12 GB', 1899.99)
]

# list of lists (2D list, matrix)

matrix = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
]

# 1 2 3
# 4 5 6
# 7 8 9

print(matrix[1])    # [4,5,6]
print(matrix[1][2]) # 6

matrix[0] = [0,1,2]

mixed_list = [
    [1, 2, 3],
    ['a', 'b', 'c']
]
print(mixed_list)   # possible but not advisable

# function

# advantages:
# 1. write less code
# 2. avoid making same mistakes many times
# 3. smaller units of code (understandable units)
# 4. testable units of code (unit testing - combined testing is integration testing)
