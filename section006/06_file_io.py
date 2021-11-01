# relative to inheritance:
# dog.py

# relative to LectureExamples:
# section006/inheritance/dog.py

# absolute:
# C:\Users\randy\Documents\Fall2021\CSCI1030U\LectureExamples\section006\inheritance\dog.py

# plain_text_file = open('section006/data/plain_text.txt', 'r')

# print(plain_text_file.readline(), end='')
# print(plain_text_file.readline())

# print(plain_text_file.read())

# for line in plain_text_file:
#     print(line)
# # programmers forget to close files a lot!
# plain_text_file.close()


with open('section006/data/plain_text.txt', 'r') as plain_text_file:
    for line in plain_text_file:
        print(line)

print('hi')

student_names = ['Chris Hemsworth', 'Bowser', 'Mr. Bean', 'Scarlet Johansson', 'Kate', 'Emily']
with open('section006/data/students_output.txt', 'w') as students_file:
    for name in student_names:
        students_file.write(f'{name}\n')

import json 

with open('section006/data/grades.json', 'r') as grades_file:
    grades = json.load(grades_file)
    print(grades['100000004'])

youtube_videos = [
    {
        'title': 'Lenny bit my finger',
        'description': 'My cat can be evil',
        'url': 'https://youtube.com/v/3947732654'
    }
]
with open('section006/data/youtube_video.json', 'w') as youtube_file:
    json.dump(youtube_videos, youtube_file)

# exceptions

class DontDivideByZeroBonehead(Exception):
    pass

def div(a, b):
    if b == 0:
        raise DontDivideByZeroBonehead('Cannot divide by zero')

    return a / b 

print(f'1/2 is {div(1, 2)}')

try:
    # result = div(1, 0) + 1
    print(f'1/0 is {div(1, 0)}')
except DontDivideByZeroBonehead as error:
    # TODO: Handle the error
    print(error)

# example of a bad use of try/except
list = [1,2,3]
try:
    print(list[3])
except IndexError as error:
    # Don't catch an error just to print it!
    print(error)

# coding exercise
try:
    for n in [5,4,3,2,1,0]:
        print(1/n)
except ZeroDivisionError as error:
    print(f'Attempted divide by zero: {error}')
finally:
    # TODO: clean up
    print('Always do this')
