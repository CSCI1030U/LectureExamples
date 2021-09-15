# Types of error:
#
# 1. Syntax error - mistake in the format of Python code
#         - very easy to find and resolve
#         - get notification in your editor
#         - your program will stop running when it encounters the error
#         - you see an error message
#         - you see the line number where the error can be found
#         - example:
# name = 'Randy

# 2. Runtime error - syntax is correct
#         - almost as easy to find and resolve as syntax errors
#         - don't get a notification in your editor
#         - your program will stop running when it encounters the error
#         - you see an error message
#         - you see the line number where the error can be found
#         - example:

course = 'CSCI1030U'
print(course[9])

# 3. Logic error - syntax is correct, no runtime errors, but does the wrong thing
#         - the most difficult error to find
#         - don't get a notification in your editor
#         - the program doesn't stop running
#         - there are no error messages
#         - you don't know the line number
#         - example:

average = (3.0 + 3.0 + 3.0 + 6.0 + 5.5 + 5.0 + 6.0) / 7
print(f'average = {average:0.3f} out of 3.0')

name = 'Randy'
print(f'My name is {name}.  Nice to meet you.')

print('you made it here!')