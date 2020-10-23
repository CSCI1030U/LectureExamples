# (0|1)*
# .*

# phone number XXX-XXXX
# \d{3}-\d{4}

# phone number (XXX-XXX-XXXX or XXX-XXXX)
# (\d{3}-)?\d{3}-\d{4}

# [a-zA-Z] - any letter (uppercase or lowercase)

# [0-9] = \d
# space, tab (\t), newline (\n) = [ \t\n] = \s
# [a-zA-Z0-9_] = \w - word character (?), more correctly: variable

# ^ - beginning of the string
# $ - end of the string
# ^(\d{3}-)?\d{3}-\d{4}$

import re

# at least three a's
re1 = re.compile('^aaa+$')
match = re1.match('aaaaa')
if match:
    print('Yes, it matches')
    print(match.group())

# binary number with 4 digits or 8 digits
re2 = re.compile('^([01]{4})|([01]{8})$')
match = re2.match('0000')
if match:
    print('Yes, it matches')
    print(match.group())
