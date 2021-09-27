# lists (insertion, removal, len, max, min, in, index, count, 2D lists), list comprehension, tuples

student_names = ['Manpreet', 'Alex', 'Sam', 'Barbara']

# adding to a list
student_names.append('Xiao')        # result: ['Manpreet', 'Alex', 'Sam', 'Barbara', 'Xiao']
student_names.insert(0, 'Margaret') # result: ['Margaret', 'Manpreet', 'Alex', 'Sam', 'Barbara', 'Xiao']
student_names.insert(6, 'Yolanda')  # result: ['Margaret', 'Manpreet', 'Alex', 'Sam', 'Barbara', 'Xiao', 'Yolanda']
student_names.insert(4, 'Margaret') # result: ['Margaret', 'Manpreet', 'Alex', 'Sam', 'Margaret', 'Barbara', 'Xiao', 'Yolanda']
print(student_names[6]) # 'Yolanda'

# removing from a list
print(f'before deleting Margaret: {student_names}')
student_names.remove('Margaret')
student_names.remove('Margaret')
print(f'after deleting Margaret: {student_names}')

student_names.pop(2)  # deletes 'Sam'
print(f'after deleting Sam: {student_names}')
student_names.pop()   # deletes 'Yolanda'
print(f'after deleting Yolanda: {student_names}')

# for name in student_names:
#     print(name)

# list membership
if 'Xiao' in student_names:
    print('Yes, Xiao is in my class')
else:
    print('No, Xiao is not on the class list')

print(student_names.index('Xiao'))

if 'Ralph' in student_names:
    print(f'Ralph is found at index {student_names.index("Ralph")}')
else:
    print('Ralph is not in the list')

print(f'The name Margaret appears {student_names.count("Margaret")} times in the list')

# other functions

print(f'the min in student_names is {min(student_names)}')
print(f'the max in student_names is {max(student_names)}')

# inadvisable_list = ['Sally', 38.0, 'Joe', 7, [1,2,3]]  # do not mix types in a list
# print(max(inadvisable_list))

# list comprehensions

# math notation:  { x | x <- I, x >= 0, x < 100 }

# this is the long way:
# list1 = []
# for x in range(0, 100):
#     list1.append(x**2)

list1 = [x**2 for x in range(0, 100)]
print(list1)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)         # whole matrix
print(matrix[0])      # whole first list [1, 2, 3]
print(matrix[2][0])   # list at index 2 ([7,8,9]), element 0 (7)

# tuples (can contain different types)

x,y = 1,2

sample1 = (906, '10mL', 10.0, '3ppm', '14ppm', ['latitude', 'longitude'])

samples = [
    (906, '10mL', 10.0, '3ppm', '14ppm', ['latitude', 'longitude']),
    (907, '9.4mL', 9.4, '11ppm', '8ppm', ['latitude', 'longitude'])
]

print(f'The mass of sample1 is {sample1[2]}')

print(samples[1][4])

# benefit of functions
# 1. code modular (small pieces)
# 2. name -> readable
# 3. smaller - easier to digest/understand
# 4. test just each function on its own