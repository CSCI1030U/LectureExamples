# practice

# plain_text_input = open('section017/data_files/plain_text_input.txt', 'r')
# # TODO: read from the file
# plain_text_input.close()

with open('section017/data_files/plain_text_input.txt', 'r') as plain_text_input:
    for line in plain_text_input:
        print(line, end='')

names = ['Sally', 'Rhonda', 'Ridge']
with open('section017/data_files/plain_text_output.txt', 'w') as plain_text_output:
    for name in names:
        plain_text_output.write(name + '\n')

import json 

with open('section017/data_files/json_input.json', 'r') as json_input:
    products = json.load(json_input)
    for prod in products:
        print(prod)

products_new = [
    {
        "product_id": 1,
        "model": "RTX 4090",
        "price": 1799.99
    },
    {
        "product_id": 2,
        "model": "RTX 4080",
        "price": 1099.99
    }
]
with open('section017/data_files/json_output.json', 'w') as json_output:
    json.dump(products_new, json_output)

# coding exercise 7.1 (output to CSV format)

sids = ['100000000', '100000001', '100000002', '100000003', '100000004', '100000005', '100000006', '100000007', '100000008', '100000009']
midterm_marks = [52.0, 48.5, 54.25, 61.5, 64.0, 77.75, 29.0, 91.25, 68.25, 59.75]

with open('section017/data_files/grade_output.csv', 'w') as csv_output:
    for index in range(len(sids)):
        csv_output.write(f'{sids[index]},{midterm_marks[index]}\n')


# coding exercise 7.2 (output 1/n for all n in the list [5,4,3,2,1,0])
class DividingByZeroIsForEngineers(Exception):
    pass

def div(a, b):
    try:
        return a / b
    except ZeroDivisionError as error:
        # bad idea to hide your errors
        print(f'Tried to divide by zero: {error}')
        raise DividingByZeroIsForEngineers('1/n for 0 is not allowed')

# for n in [5,4,3,2,1,0,-1]:
#     print(f'{div(1,n) = }')

# coding exercise 7.3 (test class for Student)

class Student:
    def __init__(self, gpa, name):
        self.gpa = gpa
        self.name = name
        self.marks = []

    def set_mark(self, course, mark):
        self.marks.append(mark)

    def get_average(self):
        if len(self.marks) == 0:
            return 0.0

        sum = 0
        for mark in self.marks:
            sum += mark
        return sum / len(self.marks)

import unittest 

class Student_Test(unittest.TestCase):
    def test_init(self):
        clarissa = Student(0.0, 'Clarissa')
        self.assertEqual(clarissa.gpa, 0.0)
        self.assertEqual(clarissa.name, 'Clarissa')
        self.assertEqual(clarissa.marks, [])

    def test_set_mark(self):
        clarissa = Student(0.0, 'Clarissa')
        self.assertTrue(clarissa.marks == [])
        clarissa.set_mark('CSCI1030U', 70.0)
        self.assertTrue(clarissa.marks == [70.0])
        clarissa.set_mark('CSCI1060U', 80.0)
        self.assertTrue(clarissa.marks == [70.0, 80.0])

    def test_get_average(self):
        clarissa = Student(0.0, 'Clarissa')
        self.assertAlmostEqual(clarissa.get_average(), 0.0)
        clarissa.set_mark('CSCI1030U', 70.0)
        self.assertAlmostEqual(clarissa.get_average(), 70.0)
        clarissa.set_mark('CSCI1030U', 80.0)
        self.assertAlmostEqual(clarissa.get_average(), 75.0)


unittest.main()