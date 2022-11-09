# practice
with open('section001/data/plain_text.txt', 'r') as plain_text_file:
    for line in plain_text_file:
        print(f'> {line}', end='')

products = ['RTX 4090', 'RTX 4080', 'RTX 4070']
with open('section001/data/products_output.txt', 'w') as products_file:
    for product in products:
        products_file.write(f'{product}\n')

import json

with open('section001/data/products_output.json', 'r') as json_input:
    products = json.load(json_input)
    print(f'{products = }')

products_new = [
    {
        "product_id": 1,
        "name": "RTX 4090",
        "price": 100000.00
    },
    {
        "product_id": 2,
        "name": "RTX 4080",
        "price": 50000.00
    }
]

with open('section001/data/products_new.json', 'w') as json_output:
    json.dump(products_new, json_output)

# coding exercise 7.1 (output to CSV format)

sids = ['100000000', '100000001', '100000002', '100000003', '100000004', '100000005', '100000006', '100000007', '100000008', '100000009']
midterm_marks = [52.0, 48.5, 54.25, 61.5, 64.0, 77.75, 29.0, 91.25, 68.25, 59.75]
with open('section001/data/student_data.csv', 'w') as student_output:
    for i in range(len(sids)):
        student_output.write(f'{sids[i]},{midterm_marks[i]}\n')

# coding exercise 7.2 (output 1/n for all n in the list [5,4,3,2,1,0])
class DontDivideByZeroSilly(Exception):
    pass

def div(a, b):
    if b == 0:
        # avoid dividing by zero
        raise DontDivideByZeroSilly(f'Denominator ({b}) cannot be zero')

    return a / b

try:
    for n in [5,4,3,2,1,0]:
        print(f'{div(1,n) = }')
except DontDivideByZeroSilly as error:
    print(f'Error when dividing the list elements: {error}')

# coding exercise 7.3 (test class for Student)

class Student:
    def __init__(self, gpa, name):
        self.gpa = gpa
        self.name = name
        self.marks = []

    def set_mark(self, course, mark):
        self.marks.append(mark)

    def get_average(self):
        sum = 0
        for mark in self.marks:
            sum += mark
        return sum / len(self.marks)

import unittest

class Student_Test(unittest.TestCase):
    def test_init(self):
        clarissa = Student(0.0, 'Clarissa')
        self.assertEqual(clarissa.name, 'Clarissa')
        self.assertEqual(clarissa.gpa, 0.0)
        self.assertEqual(clarissa.marks, [])

    def test_save_mark(self):
        clarissa = Student(0.0, 'Clarissa')
        self.assertTrue(clarissa.marks == [])
        clarissa.set_mark('CSCI1030U', 70.0)
        self.assertTrue(clarissa.marks == [70.0])
        clarissa.set_mark('CSCI1060U', 80.0)
        self.assertTrue(clarissa.marks == [70.0, 80.0])

    def test_get_average(self):
        clarissa = Student(0.0, 'Clarissa')
        clarissa.set_mark('CSCI1030U', 70.0)
        self.assertAlmostEquals(clarissa.get_average(), 70.0)
        clarissa.set_mark('CSCI1060U', 80.0)
        self.assertAlmostEquals(clarissa.get_average(), 75.0)


unittest.main()
