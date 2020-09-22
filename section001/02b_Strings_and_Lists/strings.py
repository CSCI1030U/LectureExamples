sentence = 'the dog'

print('loop 1')
for character in sentence:
    print(character)

print('loop 2')
for index in range(len(sentence)):
    print(f'{index}, {sentence[index]}')

# coding exercise (modified version)
sentence = 'the quick brown fox jumped over the lazy dog'
reverse = ''
for index in range(len(sentence) - 1, -1, -1):
    reverse += sentence[index]
print(reverse)
print(sentence[::-1])

# coding exercise (actual version)
sentence = 'the quick brown fox jumped over the lazy dog'
reverse = ''
word = ''
for character in sentence:
    if character == ' ':
        reverse = reverse + word
        word = ' '
    else:
        word += character
reverse = reverse + word

print(reverse)
print(sentence[::-1])

# coding exercise (actual version) - another way to do it
words = sentence.split(' ')
words_reverse = []
for word in words:
    words_reverse = [word] + words_reverse
print(' '.join(words_reverse))
