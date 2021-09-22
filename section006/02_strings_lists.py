# strings, lists, and tuples

# strings
course_code = 'CSCI 1030U'
course_name = 'Introduction to CS'
course_code_and_name = f'{course_code} - {course_name}'
price = 8.99
customer_message = f'The price of the item is ${price} plus tax.'


print(course_code[9])                    # last character (fragile method - any change to course_code breaks the program)
print(course_code[len(course_code) - 1]) # last character (robust method)
print(course_code[-1])                   # last character (Python shortcut; also robust)
# print(course_code[10])                   # Runtime error (string index out of range)
print(course_code[-3])                   # 3rd last character ('3')
print(course_code[-10])                  # first character
# print(course_code[-11])                  # Runtime error

# substrings using the slice operator [start:stop:step]
print(course_code[5:9])  # 1030
print(customer_message[2:len(customer_message):2])
print(customer_message[::-1])

# programming exercise - simplified version (for practice - just reverse the long way)
first_name = 'Lorenzo'

reverse_first_name = ''
for character in first_name:
    # print(c, end=',')
    reverse_first_name = character + reverse_first_name

print(f'The reverse of {first_name} is {reverse_first_name}')

# another way to do the same thing (reverse a string)

reverse_first_name = ''
for index in range(len(first_name) - 1, -1, -1):    # [0,1,2,3,4,5,6]
    # print(first_name[index], end=' ')
    reverse_first_name = reverse_first_name + first_name[index]

print(f'The reverse of {first_name} is {reverse_first_name}')

# coding exercise (reverse the order of words in a sentence)

sentence = 'the quick brown fox jumped over the lazy dog'
# expected output:  'dog lazy the over jumped fox brown quick the'

# 1. divide the string into a list of words
list_of_words = []
current_word = ''
for character in sentence:
    if character == ' ':
        # end of a word

    else:
        # not the end of a word



# 2. reverse the list of words ([::-1])
# 3. combine the word list into a single string (spaces in between)



# lists

numbers = [0,1,2,3,4,5]
test_marks = [15.0, 14.0, 11.0, 9.5, 2.5, 14.0, 13.5]
student_names = ['Barbara', 'Lucy', "Kumar", 'Steve']

# print(student_names[len(student_names) - 1])
# print(student_names[-1])

# print(student_names[::-1])