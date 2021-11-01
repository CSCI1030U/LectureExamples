# plain_text_file = open('section001/data/plain_text.txt', 'r')

# print(plain_text_file.readline(), end='')
# print(plain_text_file.readline())

# print(plain_text_file.read())


# plain_text_file.close()

with open('section001/data/plain_text.txt', 'r') as plain_text_file:
    for line in plain_text_file:
        print(f'> {line}', end='')

print('all done reading the file')

student_names = ['Kafir', 'Sally', 'Jonah']
with open('section001/data/students_output.txt', 'w') as students_file:
    for name in student_names:
        students_file.write(f'{name}\n')

import json

with open('section001/data/grades.json', 'r') as grades_file:
    grades = json.load(grades_file)
    print(f'The grade for 100000005 is {grades["100000005"]}')

products = [
    {
        'product_id': '1',
        'name': 'RTX 3090',
        'price': '$1499'
    },
    {
        'product_id': '2',
        'name': 'RTX 3080',
        'price': '$1199'
    }
]

with open('section001/data/products.json', 'w') as products_file:
    json.dump(products, products_file)

# custom error class
class DontDivideByZeroGoofball(Exception):
    pass

# exceptions
def div(a, b):
    if b == 0:
        raise DontDivideByZeroGoofball('denominator cannot be zero')

    return a / b 

print(f'1/2 is {div(1, 2)}')

num = 1
denom = 2 # 0
# ....
# notice that this try/except makes the error harder to find/fix
try:
    result = div(num, denom) + 1.0
    print(f'1/0 is {result}')
except ZeroDivisionError as error:
    print(error)
finally:
    # code executes if there is an error or not
    # clean any resources used by the try code
    print('After the exception')

# use a try/except block when the error is user-caused, and you want to guide
# them to doing it correctly

# coding exercise
try:
    for n in [5,4,3,2,1,0]:
        print(1/n)
except ZeroDivisionError as error:
    print(error)