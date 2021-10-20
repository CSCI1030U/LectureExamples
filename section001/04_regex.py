# regular expressions

# ..   - match any two characters
# a|b  - matches a, b
# (a|b)(a|b) - matches aa, ab, ba, bb
# (a|b)*     - match <blank>, a, b, aa, ab, ba, bb, aaa, aab, ...


# a+                 - matches a, aa, aaa, aaaa, ...
# (a|b)+             - matches a, b, aa, ab, ba, bb, aaa, aab, aba, ...
# (a|b+)             - matches a, b, bb, bbb, bbbb, ...
# (a|b*)             - matches a, <blank>, b, bb, bbb, bbbb, ...
# (a+|b+)            - matches a, aa, aaa, aaaa, ..., b, bb, bbb, bbbb, ...
# a?b+               - matches ab, abb, abbb, abbbb, ..., b, bb, bbb, bbbb, ...
# a{7}               - matches aaaaaaa (only)
# (a|b){4}           - matches aaaa, aaab, aaba, aabb, abaa, ...
# (a|b){2,4}         - matches aa, ab, ba, bb, aaa, aab, aba, ..., aaaa, aaab, aaba, ...
# (a|b){2}|(a|b){4}  - matches aa, ab, ba, bb, aaaa, aaab, aaba, aabb, ...

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

# [a-z_]+    - matches snake case only
# [a-zA-Z]+  - matches camel case only
# [a-zA-Z0-9_&^%$]{8,}      - matches any sequence of 8 or more of those characters

import re 

variable_regex = re.compile('[a-z_]+')
variable_match = variable_regex.match('Average_Mark')
print(f'variable_match = {variable_match}')
if variable_match:
    print(f'Variable starts at {variable_match.start()}')
    print(f'Variable ends at {variable_match.end()}')
    print(f'Variable name is {variable_match.group()}')
else:
    print(f'Did not match')

