# strings, lists, and tuples

# strings

course_name = 'CSCI1030U'
first_name = 'Randy'
cost = 79.99
message = f'The cost is ${cost} plus tax.'
# print(message)

weird_string = course_name + first_name # string concatenation
print('.' * 25)

print(first_name[0])  # first
print(first_name[1])  # second
print(first_name[4])  # last
# print(first_name[5])  # IndexError - string index out of range
print(first_name[-1]) # last (just in Python!)

for c in first_name:
    print(c)


# lists

test1_grades = [15.0, 14.5, 11.0, 2.5, 5.0, 9.0, 8.5, 4.0, 2.0, 15.0]

print(test1_grades[0])  # first
print(test1_grades[-1]) # last

test1_grades_twice = test1_grades + test1_grades  # list concatenation

student_names = ['Barbara', "Lucy", 'Kumar', 'Steve']
print(student_names * 2)

# for grade in test1_grades:
#     print(grade)

# slice operator [start:stop:step]
subset = student_names[1:3]   # create a list including elements from index 1 (inclusive) to 3 (exclusive)
# print(course_name[2:5])
num_student_names = len(student_names)
print(student_names[0:num_student_names:2])

full_name = 'Randy Fortier'
print(full_name[0:len(full_name):3])

print(full_name[::-1]) # the easy way

# the long way (for practice)
reverse_full_name = ''
for character in full_name:
    reverse_full_name = character + reverse_full_name
print(f'The reverse of {full_name} is {reverse_full_name}')

# the even longer way (practice right?)
reverse_full_name = ''
for index in range(len(full_name) - 1, -1, -1):
    # print(full_name[index], end=' ')
    reverse_full_name = reverse_full_name + full_name[index]

print(f'The reverse of {full_name} is {reverse_full_name}')

# coding exercise

sentence = 'the quick brown fox jumped over the lazy dog'

# 1. divide this sentence into words in a list
# 2. reverse the word list
# 3. join the list back into a sentence (reversed)

# this is equivalent to the split()
words = []
current_word = ''
for character in sentence:
    if character == ' ':
        words.append(current_word)
        current_word = ''
    else:
        # this character is part of a word
        current_word += character

words.append(current_word)

# error in above code  Can you figure it out? (two errors fixed)
# print(words)

# join the list of words back into the string, but in reverse

# equivalent to the function join() (except reversing the words)
reverse_sentence = ''
for word in words:
    # reverse_sentence = word + ' ' + reverse_sentence
    reverse_sentence = f'{word} {reverse_sentence}'

print(reverse_sentence)