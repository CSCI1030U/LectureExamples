def main():
    # practice

    first_name = 'Randy'
    last_name = "Fortier"
    full_name = f'{first_name} {last_name}'
    message = f'''
    Dear {first_name},

    We enjoy you're bussness.  E-Mail use your credit
    card number immediately or your account will be
    terminated.

    Seriously,
    CEO of Apple Tom Crook
    '''

    print(f'{full_name = }')

    words = message.split(' ')
    print(f'{words = }')

    print(f'{len(message) = }')

    lab_marks = [2.0, 2.5, 1.5, 2.5, 2.5, 2.5]
    print(f'{min(lab_marks) = }')

    matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
    ]

    print(f'{lab_marks = }')
    print(f'{lab_marks[2:4] = }')

    print(f'{matrix = }')
    print(f'{matrix[2] = }')
    print(f'{(matrix[2])[0] = }')

    ram = (128, 'DDR4', 2700, '$350.00')

    print(f'{ram[3] = }')

    ram_better = {
        'size': 128,
        'std': 'DDR4',
        'clock': 2700,
        'price': '$350.00',
    }

    print(f"{ram_better['price'] = }")

    # coding exercise 3.1 (reverse words)

    sentence = 'ahmed runs quickly'
    words = sentence.split(' ')
    print(f'{words = }')

    reverse_sentence = ''
    for word in words:
        reverse_sentence = word + ' ' + reverse_sentence

    print(f'{reverse_sentence = }')

    # coding exercise 3.2 (average mark)

    midterm_marks = [40.0, 50.0, 70.0]
    print(f'{sum(midterm_marks)/len(midterm_marks)=}')

    mark_sum = 0.0
    count = 0
    for mark in midterm_marks:
        mark_sum += mark
        count += 1

    print(f'{mark_sum / count = }')

    # hacker's corner

    squares = [x**2 for x in range(1000000)]
    print(f'{squares = }')


if __name__ == '__main__':
    main()
