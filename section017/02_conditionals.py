# programming exercise

principle = 100000
interest_rate = 0.035

# principle = principle + interest
# principle *= 1 + interest_rate  # another equally good way to do it

principle += principle * interest_rate
principle += principle * interest_rate
principle += principle * interest_rate
principle += principle * interest_rate
principle += principle * interest_rate
print(f'principle:{principle}')
print(f'principle:${principle:0.2f}.')

# conditionals

# commented out because it is tedious to keep entering input
# age_str = input('Enter your age:')
# age = int(age_str)

age = 14
# age = int(input('Enter your age:'))  # equivalent to above two statements

# if (age >= 10 && age < 30) {
#   ...print something...
# }

# if age >= 10 and age < 30:  # this is equivalent to the one below
if 10 <= age < 30:
    print('You can have your first pokemon!')
    print('Pikachu?')
    pokemon = 'Charizard'
elif age < 10:
    print('You will get your pokemon later!')
else:
    print('Sorry, no pokemon for you!')

x = 1
y = 2
z = 3
# if x > y:
#     maximum = x 
#     print('x')
# else:
#     maximum = y
maximum = x if x > y else y

count = 5
while count > 0:
    print(f'count == {count}')
    count = count - 1
    # count -= 1