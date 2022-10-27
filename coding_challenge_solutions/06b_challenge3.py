import re

# coding challenge - recognize an E-Mail address

# email_regex = re.compile('^[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]+$')   # simple version
email_regex = re.compile('^[a-zA-Z][a-zA-Z0-9_.]*@[a-zA-Z][a-zA-Z0-9_]*(\.[a-zA-Z][a-zA-Z0-9_])+$')   # more advanced version
# ^...  - match at the start of the string
# ...$  - match at the end of the string
# ^...$ - match the whole string
email_match = email_regex.search('stacy.smith@ontariotechu.ca')
if email_match:
    print(f'The matched E-Mail address:  {email_match.group()}')
else:
    print('No match found')
