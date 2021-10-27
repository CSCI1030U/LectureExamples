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