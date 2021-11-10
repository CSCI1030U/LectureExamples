# dictionary as a list of tuples

# {'Giselle Leclair': 221.97,
#             'Yifeng Wu': 704.18,
#             'Fred Smith': 132.09}
balances = [
    ('Giselle Leclair', 221.97),
    ('Yifeng Wu', 704.18),
    ('Fred Smith', 132.09)
]

# balances['Siaana Kaur'] = 0.0
balances.append( ('Siaana Kaur', 0.0) )

# print(balances['Siaana Kaur'])
for balance in balances:
    if balance[0] == 'Siaana Kaur':
        print(balance[1])

# stack using Python list

stack = []
print("isEmpty?", (len(stack) == 0))        # isEmpty()

stack.append(1)                             # push()
stack.append(2)                             # push()
stack.append(3)                             # push()
print("top:", stack[-1])                    # top()
print("isEmpty?", (len(stack) == 0))        # isEmpty()
print(stack)

print(stack.pop())                          # prints 3
print(stack.pop())                          # prints 2
print(stack.pop())                          # prints 1
print("isEmpty?", (len(stack) == 0))        # isEmpty()

# queue using Python lists

queue = []
queue.append(1)                                 # enqueue()
queue.append(2)                                 # enqueue()
queue.append(3)                                 # enqueue()
print("front:", queue[0])                     # front()
print("isEmpty?", (len(queue) == 0))        # isEmpty()
print(queue.pop(0))                         # prints 1
print(queue.pop(0))                         # prints 2
print(queue.pop(0))                         # prints 3
