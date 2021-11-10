# dictionary as a list of tuples

# balances = {'Giselle Leclair': 221.97,
#             'Yifeng Wu': 704.18,
#             'Fred Smith': 132.09}

balances = [
    ('Giselle Leclair', 221.97),
    ('Yifeng Wu', 704.18),
    ('Fred Smith', 132.09)
]

# balances['Siaana Kaur'] = 0.0

balances.append(('Siaana Kaur', 0.0))

num_elements = len(balances)

# for key in balances:
#     print(key, '-', balances[key])
for balance in balances:
    print(f'{balance[0]} - {balance[1]}')

# print(balances['Sianna Kaur'])
for balance in balances:
    if balance[0] == 'Sianna Kaur':
        print(balance[1])

print(balances[1])

# stack using Python list

stack = []
stack.append(1)                             # push()
stack.append(2)                             # push()
stack.append(3)                             # push()
print("top:", stack[-1])                    # top()
print("isEmpty?", (len(stack) == 0))    # isEmpty()
print(stack.pop())                         # prints 3
print(stack.pop())                         # prints 2
print(stack.pop())                         # prints 1

# queue using Python lists

