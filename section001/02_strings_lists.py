# strings, lists, and tuples

course_code = 'CSCI1030U'
course_name = 'Introduction to Computer Science'
# full_course = course_code + ' - ' + course_name
full_course = f'{course_code} - {course_name}'
# print(full_course)

name = 'Mickey'
# 1 * 50 = 1 + 1 + 1 + 1 + 1 .... 1 (50 times)
# '-' * 50 = '-' + '-' + '-' + '-' + ... + '-' (50 times)
print(name * 10)
# print('-' * 50)

# print(name[6])  # runtime error (string index out of range)
print(name[5])   # last character (fragile code - any change to 'name' breaks the program)
print(name[len(name) - 1]) # last character (robust code)
print(name[-1])            # last character (robut, but only in Python)

# slice operator [start:stop:step]  range(start, stop, step) (0, len, 1)
name = 'Mickolas M. Mouse'
print(name[0:4])
print(name[12:17])
print(name[0:10:2])
print(name[::-1])

# lists

test_marks = [18.0, 20.0, 11.0, 9.5, 4.5, 14.5, 19.0]
student_names = ['Susanne', 'Kumar', "Larry", 'Kristine']

print(student_names[-1])
print(student_names[len(student_names) - 1])
# print(student_names[5])  # runtime error (list index out of range)

# coding exercise (easier version)

sentence = 'abcde'
reversed_sentence = ''
for ch in sentence:
    reversed_sentence = ch + reversed_sentence 

print(f'{sentence} reversed is {reversed_sentence}')

# coding exercise (full version from slide 13)

sentence = 'the quick brown fox'
# expected result:  'fox brown quick the'

# 1. converted the single string 'sentence' into a list of words

# expected:  word_list = ['the', 'quick', 'brown', 'fox']
word_list = []
word = ''
for character in sentence:
    if character == ' ':
        # end of a word
        word_list.append(word)
    else:
        # not at the end of a word
        word += character
print(word_list)

# 2. reverse the list of words



# 3. combine the word list back into a single string, words separated by a space




