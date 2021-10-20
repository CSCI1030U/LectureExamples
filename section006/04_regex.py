# regular expressions

# a|b        => a, b
# (a|b)(a|b) => aa, ab, ba, bb
# (a|b)*     => <blank>, a, b, aa, ab, ba, bb, aaa, ...
# (a|b)*.*(a|b)* => <blank>?!aaab, a!9bb, aaa, b7654!bb, ...
# (a|b)+         => a, b, aa, ab, ba, bb, aaa, aab, aba, ...
# (a|b)?c+       => acccc, bc, cccc
# (a|b){4}       => aaaa, aaab, aaba, ...
# (a|b){2,3}     => aa, ab, ba, bb, aaa, aab, aba, ...
# (0|1|2|3|4|5|6|7|8|9)
# [0123456789]
# [0-9]
# [a-zA-Z]
# [ab]
# \.*  => <blank>, ., .., ..., .... (etc)
# [?.] => ?, .
# [^.,;:'"]     (any non-punctuation character)
# [^0-9]        (any non-digit character)
# [^a-zA-Z]     (any non-letter character)
# \s            (space, tab, newline, equivalent to [ \t\n])
# \w            ("word character", equivalent to [a-zA-Z0-9_])
# \d            (digit character, [0-9])
# [a-zA-Z_]\w*         (any variable name)
# [a-z_][a-z0-9_]*     (snake case variable name)
# [a-zA-Z][a-zA-Z0-9]* (camel case variable name)

import re 

# finding a single match
number_regex = re.compile('[0-9]+')
number_match = number_regex.search('there were 341 little pigs')
print(number_match)
if number_match:
    print(f'String starts at index {number_match.start()}')
    print(f'String ends at index {number_match.end()}')
    print(f'String found is {number_match.group()}')
else:
    print('No match')

# finding multiple matches
review = "I bought this product for $100.  It wasn't even worth $1."
price_regex = re.compile('\$[0-9]+')
matches = price_regex.findall(review)
print(f'matches = {matches}')

# substitution
censored_review = re.sub(price_regex, '$UNKNOWN', review)
print(f'censored review = {censored_review}')

# split
punctuation_regex = re.compile('[.,;:?!]')
sentence = 'It was the best of times; it was the worst of times. It was '
result = re.split(punctuation_regex, sentence)
print(f'result = {result}')

# password rules
password_regex = re.compile('[a-zA-Z0-9?.<>;:!@&^%$]{8,}')

# coding exercise - recognize a binary number of 8 or 16 digits

# ^ - start of the string
# $ - end of the string
# ^...$ - match the whole string only
binary_regex = re.compile('^[01]{8}([01]{8})?$')
binary_match = binary_regex.search('01101001')
if binary_match:
    print(f'The binary number starts at   {binary_match.start()}')
    print(f'The binary number ends at     {binary_match.end()}')
    print(f'The binary number matched was {binary_match.group()}')
else:
    print('No match found')
    