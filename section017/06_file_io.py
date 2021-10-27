with open('data/plain_text.txt', 'r') as plain_text_file:
    for line in plain_text_file:
        print(line, end='')
# plain_text_file.close()

print('Read all at once:')
with open('data/plain_text.txt', 'r') as plain_text_file:
    print(plain_text_file.read())

student_names = ['Pierre Trudeau', "Peter O'Toole", 'Jagmeet Singh', 'Blackbeard', 'John A. MacDonald']
with open('data/students_output.txt', 'w') as students_file:
    for index in range(len(student_names)):
        students_file.write(f'{index + 1},{student_names[index]}\n')
