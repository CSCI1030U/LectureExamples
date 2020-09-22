names = ['Sandra', 'Kunal', 'Mohammed', 'Wendy', 'Jules']
for name in names:
    print(name)

midterm_grades = [38.5, 56.0, 66.5, 95.0, 72.0, 26.0, 52.0]
total = 0.0
for grade in midterm_grades:
    total = total + grade
print('Total for the midterm:', total)
print('Average for the midterm:', total / len(midterm_grades))

sentence = 'the quick brown fox jumps over the lazy dog'
words = []
current_word = ''
for character in sentence:
    if character == ' ':
        # the end of a word, add the word to our words list
        # words.append(current_word)
        words.insert(0, current_word)
        current_word = ''
    else:
        # part of a word, add it to our current_word
        current_word = current_word + character

# words.append(current_word)
words.insert(0, current_word)

print(f'words: {words}')
print('using split:', sentence.split(' '))

# words.remove('the')
# words.pop(0)
# words.pop()
# print(f'words2: {words}')
'''
Functions
- take inputs
- produce outputs
- let you reuse your code
- can 'call' functions from many places
- all code to do that one thing is in one place
'''

[1,2,3,4]
'abcdef'
('John', 'Smith', '100000000', 3.95)

def average(values):
    total = 0.0
    for grade in values:
        total = total + grade
    return total / len(values)

midterm_grades = [38.5, 56.0, 66.5, 95.0, 72.0, 26.0, 52.0]
print('Average1:', average(midterm_grades))

test_values = [0, 5, 10]
print('Average2:', average(test_values))

one_value = [3]
print('Average3:', average(one_value))

# coding exercise
def shift(character, shift_amount):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    char_index = alphabet.index(character)
    new_index = char_index + shift_amount

    if new_index < 0:
        new_index += len(alphabet)

    if new_index >= len(alphabet):
        new_index -= len(alphabet)

    return alphabet[new_index]

def caesar_cipher(message, shift_amount):
    ciphertext = ''
    for character in message:
        encrypted_character = shift(character, shift_amount)
        ciphertext += encrypted_character
    return ciphertext

message = 'meetmeatthezoo'
print(f'{message} encrypted using the caesar cipher is:', caesar_cipher(message, 1))

c = 'a'
print(f'{c} shifted is', shift(c, 1))
