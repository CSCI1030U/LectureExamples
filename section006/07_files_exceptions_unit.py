# practice

# plain_text_input_file = open('section006/data/plain_text.txt', 'r')
# # read from the file
# plain_text_input_file.close()

with open('section006/data/plain_text.txt', 'r') as plain_text_input_file:
    # read from the file    
    for line in plain_text_input_file:
        print(line, end='')

student_names = ['Sally', 'Rhonda', 'Rupert']
with open('section006/data/plain_text_output.txt', 'w') as plain_text_output_file:
    for name in student_names:
        plain_text_output_file.write(name + '\n')

import json 

with open('section006/data/products_input.json', 'r') as json_input_file:
    products = json.load(json_input_file)
    for product in products:
        print(f'{product = }')

products = [
    {
        "product_id": 1,
        "model": "RTX 4090",
        "price": 1799.99
    },
    {
        "product_id": 2,
        "model": "RTX 4080",
        "price": 1299.99
    }
]
with open('section006/data/products_output.json', 'w') as json_output_file:
    json.dump(products, json_output_file)

# coding exercise 1 (output to CSV format)

sids = ['100000000', '100000001', '100000002', '100000003', '100000004', '100000005', '100000006', '100000007', '100000008', '100000009']
midterm_marks = [52.0, 48.5, 54.25, 61.5, 64.0, 77.75, 29.0, 91.25, 68.25, 59.75]

with open('section006/data/student_data.csv', 'w') as student_data_output_file:
    for index in range(len(sids)):
        student_data_output_file.write(f'{sids[index]},{midterm_marks[index]}\n')

# coding exercise 2 (output 1/n for all n in the list [5,4,3,2,1,0])
class DividingByZeroIsForFools(Exception):
    pass

# values = [5,4,3,2,1,0]
# for n in values:
#     # try:
#     print(f'{1/n = }')
#     # except ZeroDivisionError as error:
#     #     print(f'Error when calculating 1/n: {error}')

print('All done exercise 2!')

# coding exercise 3 (test class for Student)

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
        clarissa.set_mark('CSCI1030U', 90.0)
        self.assertEqual(len(clarissa.marks), 1)
        self.assertEqual(clarissa.marks[0], 90.0)

    def test_get_average(self):
        clarissa = Student(0.0, 'Clarissa')
        self.assertAlmostEqual(clarissa.get_average(), 0.0)
        clarissa.set_mark('CSCI1030U', 70.0)
        self.assertAlmostEqual(clarissa.get_average(), 70.0)
        clarissa.set_mark('CSCI1030U', 80.0)
        self.assertAlmostEqual(clarissa.get_average(), 75.0)

unittest.main()