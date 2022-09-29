# coding challenge solution

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

# more advanced solution for coding exercise 1 (without using split())
sentence = 'ahmed runs quickly'
reverse = ''
current_word = ''
for character in sentence:
    if character == ' ':
        # this is a delimiter, so add the characters in the current word to the reversed sentence
        reverse = current_word + ' ' + reverse 
        current_word = ''
    else:
        current_word += character
# add the final word (which has no following delimiter)
reverse = current_word + ' ' + reverse 

print(f'{reverse.strip() = }')
