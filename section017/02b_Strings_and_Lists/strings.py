course = 'CSCI 1030U-017'
description = '''
This course introduces a broad range of concepts from the different areas of computer science. Topics
covered include problem solving, data structures and algorithms from areas such as artificial intelligence,
computer architecture, networking and the Internet.
'''

print('slice1:')
print(course[0])
print(course[1])
print(course[-1])
print(course[-2])

print('slice2:')
print(course[1:6])
print(course[:3])
print(course[3:])

print('slice3:')
print(course[2::2])
print(course[::-1])

print(len(course))
part1 = 'CSCI'
part2 = '1030U'
print(part1 + part2)
print(part1 * 3)

# for i in range(10):
#     for j in range(10):
#          print('hello')
level = 22
print('    ' * level + 'print()')

for ch in course:
    print(ch)

print('-' * 100)

for i in range(len(course)):
    print(course[i])

# coding exercise (modified version) - reverse a string
sentence = 'the quick brown fox jumped over the lazy dog'
reversed = ''
for character in sentence:
    reversed = character + reversed

sentence = 'the quick brown fox jumped over the lazy dog'
reversed2 = ''
for i in range(len(sentence) - 1, -1, -1):
    reversed2 = reversed2 + sentence[i]

print(reversed2)
print(sentence[::-1])

# coding exercise (actual version) - reverse the order of the words in the string
words = sentence.split(' ')
words_reverse = []
for word in words:
    words_reverse = [word] + words_reverse
print(' '.join(words_reverse))
