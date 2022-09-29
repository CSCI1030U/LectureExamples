from functools import total_ordering


def main():
    print('Hello from the main function!')

    # practice
    first_name = 'Randy'
    last_name = "Fortier"
    full_name = f'{last_name}, {first_name}'

    spam = f"""
    Dear {first_name},

    We apreciate you're bussiness, but you must confirm
    your account by sending your password to us immediately!

    Regards,
    Arnold Swarzaneggar, CEO Tesla Inc.    
    """

    words = spam.split(' ')
    print(f'{words = }')

    print(f'{len(spam) = }')

    length_of_spam = 0
    for character in spam:
        length_of_spam += 1

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    print(f'{alphabet[0] = }')
    print(f'{alphabet[-1] = }')
    # print(f'{alphabet[26] = }') # index error (no such index)
    print(f'{alphabet[5:10] = }')
    print(f'{alphabet[5:15:2] = }')
    print(f'{alphabet[::] = }')   # copy
    print(f'{alphabet[::-1] = }') # reverse
    
    prices = [299.99, 99.99, 19.99, 449.99]
    print(f'{min(prices) = }')

    prices.append(1099.99)

    ram1 = 64, 'Overheatsalot Inc.', 2700, '$499.99'

    print(f'{ram1[3] = }')
    for val in ram1:
        print(f'{val = }')

    ram2 = {
        'brand': 'Overheatsalot Inc.',
        'size': 64, 
        'speed': 2700,
        'price': '$499.99'
    }

    print(f'{ram2["price"] = }')

    for key in ram2:
        print(f'\t{key} => {ram2[key]}')

    # hacker's corner
    gen1 = (x**2 for x in range(100000))  # on demand
    list1 = [x**2 for x in range(100000)] # pre-generated

    # coding exercise 1 (reverse words)
    sentence = 'ahmed runs quickly'
    words = sentence.split(' ')
    reverse = ''
    for word in words:
        # reverse = reverse + word # wrong order
        # reverse += word
        reverse = word + ' ' + reverse

    print(f'{reverse = }')

    # coding exercise 2 (average mark)

    marks = [50.0, 65.0, 77.5, 80.0]

    total_marks = 0.0
    count = 0
    for mark in marks:
        total_marks += mark
        count += 1
    print(f'{total_marks / count = }')

    print(f'{sum(marks) / len(marks) = }')

main()