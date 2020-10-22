import re 

# re1 = re.compile('^a*$')
# match = re1.match('aaa')
# if match:
#     print('It matches!')
#     print('Match string: ', match.group())

# re2 = re.compile('^bba+$')
# match = re2.match('bbaaa')
# if match:
#     print('It matches!')
#     print('Match string: ', match.group())

# binary number with either 4 digits or 8 digits
# re3 = re.compile('^(([01]{4})|([01]{8}))$')
re3 = re.compile('^(([01]{4})([01]{4})?)$')
# match = re3.match('0011')
# if match:
#     print('It matches!')
#     print('Match string: ', match.group())
# else:
#     print('No match')

# recognize first name, middle name, last name (e.g. Barb Elan Jones) [A-Z]
re4 = re.compile('^([A-Z][a-z]+\s){2}([A-Z][a-z]+)$')
match = re4.match('James Earl Jones')
if match:
    print('It matches!')
    print('Match string: ', match.group())

