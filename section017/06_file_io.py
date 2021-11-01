with open('section017/data/plain_text.txt', 'r') as plain_text_file:
    for line in plain_text_file:
        print(line, end='')
# plain_text_file.close()

print('Read all at once:')
with open('section017/data/plain_text.txt', 'r') as plain_text_file:
    print(plain_text_file.read())

student_names = ['Pierre Trudeau', "Peter O'Toole", 'Jagmeet Singh', 'Blackbeard', 'John A. MacDonald']
with open('section017/data/students_output.txt', 'w') as students_file:
    for index in range(len(student_names)):
        students_file.write(f'{index + 1},{student_names[index]}\n')


class DontDivideByZeroYouBonehead(Exception):
    pass

def div(a,b):
    if b == 0:
        raise DontDivideByZeroYouBonehead('ERROR:  Cannot divide by zero')

    return a/b

print(f'1/2 is {div(1,2)}')

# result = div(1,0) + 1
# print(f'1/0 is {result}')

class APIUsageError(Exception):
    pass

def convert_usd_to_cad(amount):
    # TODO: Use an online web API to convert
    raise APIUsageError(f'Tried to convert {amount} to CAD, but the API was used incorrectly')
    return amount * 1.27

total = 39.99
try:
    print(f'The total is ${convert_usd_to_cad(total)} (CAD)')
except APIUsageError as error:
    print(error)

try:
    for n in [5,4,3,2,1,0]:
        print(1/n)
except ZeroDivisionError as error:
    print(f'Tried to divide by zero: {error}')