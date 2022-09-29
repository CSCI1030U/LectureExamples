sentence = 'ahmed runs quickly'
word = ''
words = []
for character in sentence:
    if character == ' ': # delimiter
        words.append(word)
        word = ''
    else:
        word += character
words.append(word) # the final word has no delim

print(f'{words = }')