# coding exercise

principle = 100
interest_rate = 0.035

# interest = principle * interest_rate
# principle = principle + interest

principle += principle * interest_rate
principle += principle * interest_rate
principle += principle * interest_rate
principle += principle * interest_rate
principle += principle * interest_rate

# print('principle=$' + str(principle) + '.')  # not as nice
print(f'principle=${principle:10.2f}.')

# conditionals

age = 120
if age > 100:
    print('Dude, you are too old for a pokemon!')
elif age >= 10:
    print('Choose your pokemon')
else:
    print('Sorry but you are too young to have pokemon, youngster')

a,b = 7,11

# totally unnecessary, but cool shortcut for conditionals

# unary operator:  -(x+y)  (negates its one operand)
# binary operator:  x+y    (adds its two operands together)
# ternary operator:
print(a if a < b else b)

# loops

num_repetitions = 5
while num_repetitions > 0:
    print(f'num_repetitions = {num_repetitions}')
    # num_repetitions = num_repetitions - 1
    num_repetitions -= 1