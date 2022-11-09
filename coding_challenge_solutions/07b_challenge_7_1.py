# coding challenge 7.1

class TooYoungError(Exception):
    pass

age_str = input('How old are you?')
age = int(age_str)
if age < 18:
    raise TooYoungError('You must be at least 18 to vote')
else:
    print('You can vote now')
