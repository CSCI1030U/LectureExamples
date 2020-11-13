balances = [
    ('Giselle Leclair', 221.97),
    ('Yifeng Wu', 704.18),
    ('Fred Smith', 132.09)
]
balances.append(('Siaana Kaur', 0.0))

for name, balance in balances:
    print(f"{name}'s balance is ${balance}")

name_stack = []
name_stack.append('Albert')
name_stack.append('Barbara')
name_stack.append('Carla')

while len(name_stack) > 0:
    print(name_stack.pop())

# expression = '((1+2)*(3/4))'
expression = '())('

stacket = []
for ch in expression:
    if ch == '(':
        stacket.append(ch)
    elif ch == ')':
        if len(stacket) > 0:
            stacket.pop()
        else:
            print('Invalid expression: unmatched ")"')
            break
if len(stacket) != 0:
    print('Invalid expression: unmatched "("')

customers_queue = []
customers_queue.append('Albert')
customers_queue.append('Barbara')
customers_queue.append('Carla')
while len(customers_queue) > 0:
    print(customers_queue.pop(0))