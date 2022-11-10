# practice

first_name = 'Randy'
last_name = "Fortier"
full_name = f'{last_name}, {first_name}'

spam = f"""
Dear {first_name},

We are please to have you as a customer.  

Sned money to use to prove who you are before we cancel your account.

Regards,
CEO TD Bank, Charlize Theron
"""

print(f'{full_name = }')
print(f'{spam = }')

# for ch in full_name:
#     print(f'{ch = }')

full_name = 'Fortier, Randy'
print(f'{full_name[0] = }')
print(f'{full_name[-1] = }')
print(f'{full_name[0:8:2] = }')

words = spam.split(' ')
print(f'{words = }')

print(f'{len(spam) = }')
print(f'{len(words) = }')

prices = [299.99, 19.99, 159.99, 164.49]
total_price = 0.00
for price in prices:
    total_price += price

print(f'{sum(prices) / len(prices) = }')

prices.append(999.99)

ram1 = 64, 'Gonnabreaksoon', 2700, '$219.99'

# some_function((1,'abc',2.99))

print(f'{ram1[-1] = }')
# print(f'{ram1[4] = }') # index error (no such index)

ram2 = {
    'brand': 'Gonnabreaksoon', 
    'size': 64, 
    'speed': 2700,
    'price': '$219.99',
}

print(f"{ram2['price'] = }")

for key in ram2:
    print(f'\t{key = } => {ram2[key] = }')

# coding exercise 3.1 (reverse words)

sentence = 'ahmed runs quickly'
words = sentence.split(' ')
reverse = ''
# for index in range(len(words) - 1, -1, -1):
#     # reverse = reverse + word
#     reverse += words[index] + ' '
for word in words[::-1]:  # words[::-1] is the reverse of words
     reverse += word + ' '

print(f'{reverse = }')

# coding exercise 3.2 (average mark)

midterm_marks = [50.0, 60.0, 85.0]
print(f'{sum(midterm_marks) / len(midterm_marks) = }')

# hacker's corner

gen1 = (x**2 for x in range(100000)) # on demand
list1 = [x**2 for x in range(100000)] # pre-generated
