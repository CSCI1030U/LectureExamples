marks_dictionary = [('100000001', 67.5), ('100000002', 70.0)]
marks_dictionary.append(('100000003', 75.5))
print(marks_dictionary)

sid_to_find = '100000003'
for sid, mark in marks_dictionary:
    if sid == sid_to_find:
        print(mark)

if ((1+2)*(3+(8-3))):
    pass

expression = '((1+2)*(3+(8-3)))'
# expression = '(((1+2)*(3+(8-3)))'
# expression = '((1+2)*(3+(8-3))))'
# expression = ')('

# if I find a '(', push onto a stack
# if I find a ')', pop something off the stack
bracket_stack = []
for c in expression:
    if c == '(':
        bracket_stack.append(c)
    elif c == ')':
        if len(bracket_stack) > 0:
            bracket_stack.pop()
        else:
            print('Error: Unmatched ")"')
            break

if len(bracket_stack) != 0:
    print('Error: unmatched "("')
