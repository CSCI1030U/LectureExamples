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