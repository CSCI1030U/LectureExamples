# regular expressions

# 0123456789 - match only '0123456789'
# [0123456789] - matches 0 or 1 or 2 or 3 or ...
# [0-9]
# [a-z]+
# [^a-z]
# [^0123456789]
# \s - any whitespace (tab, space, newline)
# \w - any "word"
# \d - any digit [0-9]

# [a-zA-Z_]\w*

import re 

regex1 = re.compile('\$\d+')
match1 = regex1.search('I paid $100 for this item.  It was not even worth $1')
print(f'The result of search() is {match1}')
if match1:
    print(f'The string matches!')
    print(f'The matched string: {match1.group()}')

new_review = re.sub(regex1, '$UNKNOWN', 'I paid $100 for this item.  It was not even worth $1')
print(f'The censored review is {new_review}')

name_regex = re.compile('[A-Z][a-z]*')
name_match = name_regex.match('John Jonah Jameson')
if name_match:
    print(f'Start index:    {name_match.start()}')
    print(f'End index:      {name_match.end()}')
    print(f'Matched string: {name_match.group()}')
print(f'All names are: {name_regex.findall("John Jonah Jameson")}')

punctuation_regex = re.compile('[.,:;!?]')
result = re.split(punctuation_regex, 'It was the best of times; it was the worst of times.')
print(result)

# coding exercise - recognize a binary number of 8 or 16 digits

binary_regex = re.compile('^[01]{8}([01]{8})?$')
binary_match = binary_regex.search('01101001')
if binary_match:
    print(f'Start of the binary number: {binary_match.start()}')
    print(f'End of the binary number:   {binary_match.end()}')
    print(f'The matched binary number:  {binary_match.group()}')
else:
    print('No match found')

# a(ba)*b
# => ababababab
# => ab
# => abab
