names = ['Alexandra', 'Charlie', 'Khaled']
sids = ['100000000', '100000001', '100000002']
marks = [75.0, 45.0, 90.0]
grades = ['B', 'F', 'A']

with open('class_list.csv', 'w') as output_file:
    for i in range(len(names)):
        output_file.write(f'{sids[i]},{names[i]},{marks[i]},{grades[i]}\n')

with open('class_list.csv', 'r') as input_file:
    for line in input_file:
        print(line, end='')

import json 

grades = {
    '100000001': 'F',
    '100000002': 'C',
    '100000003': 'C+',
    '100000004': 'B-',
    '100000005': 'A+',
    '100000006': 'D',
    '100000007': 'A-',
    '100000008': 'B',
    '100000009': 'C'
}
with open('names.json', 'w') as output_json:
    json.dump(names, output_json)

with open('names.json', 'r') as input_json:
    list_of_names = json.load(input_json)
    for name in list_of_names:
        print(name)

index = 5
try:
    print(names[index])
except IndexError as e:
    print(f'No such index {index} - {e}')


class InvalidFilenameError(Exception):
    pass

filename = input('Enter a file name for your save file: ')
try:
    if len(filename) > 8:
        raise InvalidFilenameError('Filename is too long!')
except InvalidFilenameError as error:
    print('There are too many characters in that filename.')
    quit()

print('More stuff....')