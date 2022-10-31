# reference

# regular expressions

# ..   - match any two characters
# a|b  - matches a, b
# (a|b)(a|b) - matches aa, ab, ba, bb
# (a|b)*     - match <blank>, a, b, aa, ab, ba, bb, aaa, aab, ...

# a*                 - matches <blank>, a, aa, aaa, aaaa, ...
# a+                 - matches a, aa, aaa, aaaa, ...
# (a|b)+             - matches a, b, aa, ab, ba, bb, aaa, aab, aba, ...
# (a|b+)             - matches a, b, bb, bbb, bbbb, ...
# (a|b*)             - matches a, <blank>, b, bb, bbb, bbbb, ...
# (a+|b+)            - matches a, aa, aaa, aaaa, ..., b, bb, bbb, bbbb, ...
# a?b+               - matches ab, abb, abbb, abbbb, ..., b, bb, bbb, bbbb, ...
# a{7}               - matches aaaaaaa (only)
# (a|b){4}           - matches aaaa, aaab, aaba, aabb, abaa, ...
# (a|b){2,4}         - matches aa, ab, ba, bb, aaa, aab, aba, ..., aaaa, aaab, aaba, ...
# (a|b){4}|(a|b){2}  - matches aa, ab, ba, bb, aaaa, aaab, aaba, aabb, ...

# (a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z)  - long and inconvenient, so we need shortcuts
# [abcdefghijklmnopqrstuvwxyz]
# [a-z]      - matches a, b, c, d, e, f, ..., z
# [0-9]      - matches 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# \d         - any digit character (as above)
# [a-zA-Z]   - matches a, b, c, d, e, f, ..., z, A, B, C, D, E, F, ..., Z
# [a-zA-Z]+  - matches a, A, b, B, c, C, d, D, ..., aa, aA, ab, aB, ...
# [abc]      - matches a, b, c
# [^abc]     - matches any character, except a, b, and c
# [^0-9]     - matches any non-digit character
# [.,;:?!]   - matches any punctuation character
# \w         [a-zA-Z0-9_]  - any character that can be in a variable name
# \s         - matches space, tab, or newline

# [a-z_]+    - matches snake case only (e.g. snake_case)
# [a-zA-Z]+  - matches camel case only (e.g. camelCase)
# [a-zA-Z0-9_&^%$]{8,}      - matches any sequence of 8 or more of those characters


# practice

import re 

price_fsa = re.compile('\$[0-9]+\.[0-9]{2}')
# price_match = price_fsa.match('max_price = current_price')
price_match = price_fsa.search('I bought this product for $99.99 back in 2020, but......')

print(f'{price_match = }')
if price_match:
    print(f'\t{price_match.start() = }')
    print(f'\t{price_match.end() = }')
    print(f'\t{price_match.group() = }')
else:
    print('\tNo match found')

snake_fsa = re.compile('[a-z_]+')
snake_match = snake_fsa.search('   max_price = current_price')

print(f'{snake_match = }')
if snake_match:
    print(f'\t{snake_match.start() = }')
    print(f'\t{snake_match.end() = }')
    print(f'\t{snake_match.group() = }')
else:
    print('\tNo match found')

# coding exercise - recognize a binary number (sequence of 1s and 0s) 8 or 16 chars long

binary_fsa = re.compile('[01]{16}|[01]{8}')
binary_match = binary_fsa.search('0000111100001111')

print(f'{binary_match = }')
if binary_match:
    print(f'\t{binary_match.start() = }')
    print(f'\t{binary_match.end() = }')
    print(f'\t{binary_match.group() = }')
else:
    print('\tNo match found')