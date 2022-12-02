# exercise 10.1 (estimate prob of tails 4/5)
import numpy as np

def is_tails(value):
    if value < 0.5:
        return True 
    else:
        return False

def prob_4_of_5_tails(num_iterations):
    num_wins = 0
    for iteration in range(num_iterations):
        flip_vals = np.random.random(5)
        # flips = map(is_tails, flip_vals)
        flips = map(lambda val : val < 0.5, flip_vals)
        if list(flips).count(True) >= 4:
            num_wins += 1
    return num_wins / num_iterations

print(f'{prob_4_of_5_tails(10000) = }')

# exercise 10.2 (estimate prob of 2/5 sixes on d6)
def to_die_roll(value):
    if value < 1/6:
        return 1
    elif value < 2/6:
        return 2
    elif value < 3/6:
        return 3
    elif value < 4/6:
        return 4
    elif value < 5/6:
        return 5
    else:
        return 6

def prob_2_of_5_sixes(num_iterations):
    num_wins = 0
    for i in range(num_iterations):
        roll_vals = np.random.random(5)
        rolls = map(to_die_roll, roll_vals)
        if list(rolls).count(6) >= 2:
            num_wins += 1
    return num_wins / num_iterations

print(f'{prob_2_of_5_sixes(10000) = }')

# exercise 10.3 (estimate prob of birthday prob)
import random 

def has_duplicates(values):
    for element in values:
        if values.count(element) > 1:
            return True 
    return False

def simulate_birthday_problem(num_iterations, max_group_size):
    probabilities = {}

    # try all group sizes between 2 and max_group_size
    for group_size in range(2, max_group_size + 1):
        num_wins = 0
        # try the same simulation many times to determine the probability
        for iteration in range(num_iterations):
            birthdays = []
            # generate the birthdays for everyone in the group
            # for person in range(group_size):
            #     birthdays.append(random.randint(0, 364))
            birthday_values = np.random.random(group_size)
            birthdays = list(np.floor(birthday_values * 365))
            
            # did we find a match?
            if has_duplicates(birthdays):
                num_wins += 1
        
        probabilities[f'group-size-{group_size}'] = num_wins / num_iterations
    return probabilities

print(f'{simulate_birthday_problem(2000, 65) = }')