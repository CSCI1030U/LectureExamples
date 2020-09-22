names = ['Roberta', 'Carlos', 'Hanan', 'Julius', 'Bertha']
for name in names:
    print(name)

midterm_marks = [100.0, 75.0, 65.5, 91.0, 82.0, 70.0, 65.0, 95.5]
total = 0.0
for mark in midterm_marks:
    total += mark # total = total + mark
average = total / len(midterm_marks)

s = f'The average is {average}.'
print(s)

# 'abc' + 'def' => 'abcdef'
# 'def' + 'abc' => 'defabc'

sentence = 'the quick brown fox jumps over the lazy dog'
# => ['the', 'quick', 'brown', ...]
words = []
current_word = ''
for ch in sentence:
    if ch == ' ':
        words.append(current_word)
        # words.insert(0, current_word) # reverses the order of the words in the list
        current_word = ''
    else:
        # current_word = ch + current_word # reverses the letters in the words
        current_word = current_word + ch

# these are equivalent:
words.append(current_word)
# words = words + [current_word]

# these are also equivalent:
# words.insert(0, current_word)
# words = [current_word] + words

print(f'words = {words}')

values = ['a', 'b', 'c', 'd', 'e', 'b']
# values.remove('b')
# values.pop(2)
values.pop()
print(f'values = {values}')

# lists: [1,2,3,4,5], [[1,2,3],[4,5,6]]
# string: 'abc', 'a'
# tuple:  
student = ('Randy', 'Fortier', '100000000', 0.01)
student = 'Randy', 'Fortier', '100000000', 3.5

student_firstname = 'Randy'
student_lastname = 'Fortier'
student_sid = '100000000'
student_gpa = 3.5

# functions

def average(values):
    # sum all the values
    total = 0.0
    for mark in values:
        total += mark # total = total + mark

    # calculate the mean
    average = total / len(values)
    return average


midterm_marks = [100.0, 75.0, 65.5, 91.0, 82.0, 70.0, 65.0, 95.5]
print('The midterm average is', average(midterm_marks))
