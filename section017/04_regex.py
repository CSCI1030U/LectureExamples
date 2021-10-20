# regular expressions

# [0123456789]
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

