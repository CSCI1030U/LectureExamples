principle = 5000
interest_rate = 0.035

# interest = principle * interest_rate
# principle = principle + interest    # this is equivalent to below
# principle *= 1 + interest_rate      # equivalent, but less readable
principle += principle * interest_rate
principle += principle * interest_rate
principle += principle * interest_rate
principle += principle * interest_rate
principle += principle * interest_rate

x = 8
# string = '-' + str(x) + '-'   # -8-
string = f'-{x}-'
print(f'string = {string}')

print(f'principle:${principle:0.4f}!')

cost = 0.75
print(f'it costs ${cost:0.2f}')


# age_str = input('Enter your age:')
# age = int(age_str)
age = 10

if age > 40:
    print('You are too old to have a pokemon :(')
elif age >= 10:
    print('Choose your pokemon!')
else:
    print('You have to wait until you are 10 years old')

final_mark = 100
if final_mark >= 80:
    grade = 'A'
elif final_mark >= 70:
    grade = 'B'
elif final_mark >= 60:
    grade = 'C'
elif final_mark >= 50:
    grade = 'D'
else:
    grade = 'F'
print(f'The mark {final_mark} is a {grade} grade')
