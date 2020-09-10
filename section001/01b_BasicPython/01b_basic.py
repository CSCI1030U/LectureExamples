print(8)
print('CSCI 1030U')
print("This is Randy's program")

# yuck!  Don't do this, please
print('''Randy was here



yes he was!''')

age = 20
age = 'Randy'
print(age)

# syntax error - invalid python
# print('Randy)

# runtime error - valid python, but incorrect action
# average_age = (20 + 21 + 19) / 0

# logic error - valid python, correct behaviour, but incorrect computation
# Note: Doesn't generate an error at all, just computes the wrong value (should be 20)
average_age = (20 + 21 + 19) / 2
print(average_age)
