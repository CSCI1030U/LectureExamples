# numpy practice
import numpy as np
import math

a1 = np.array([1.2, 2.1, -0.5, 7.0])
a2 = np.zeros((8,2))
a3 = np.random.random((2,3,4))

digits = np.arange(0, 10, 1)
by_half = np.arange(0, 2 * math.pi, 0.5)
x_coords = np.linspace(0, 2 * math.pi, 50)

times_2 = x_coords * 2
y_coords = np.sin(x_coords)

coeff = np.array([
    [2,4,3],
    [1,5,1],
    [3,2,2],
])
values = np.array([5,8,4])
# print(f'{np.linalg.solve(coeff, values) = }')

# exercise 10.1 (estimate prob of tails 4+/5)
def prob_of_4_of_5(num_iterations):
    num_wins = 0

    # run the simulation multiple times
    for iteration in range(num_iterations):
        flip_vals = np.random.random(5)
        flips = map(lambda f : f < 0.5, flip_vals)
        tails_count = list(flips).count(True)
        if tails_count >= 4:
            num_wins += 1

    return num_wins / num_iterations

print(f'{prob_of_4_of_5(10000) = }')


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

def prob_of_2_6s(num_iterations):
    num_wins = 0

    for iteration in range(num_iterations):
        roll_values = np.random.random(5)
        rolls = map(to_die_roll, roll_values)
        if list(rolls).count(6) >= 2:
            num_wins += 1

    return num_wins / num_iterations

print(f'{prob_of_2_6s(10000) = }')

# exercise 10.3 (estimate prob of birthday prob)
import random

def has_duplicates(elements):
    for element in elements:
        if elements.count(element) > 1:
            return True
    return False

def has_duplicates(elements):
    for element in elements:
        if elements.count(element) > 1:
            return True
    return False

def simulate_birthday_problem(num_iterations):
    probabilities = []

    for n in range(2, 55):
        num_wins = 0
        for iteration in range(num_iterations):
            birthdays = []
            for person in range(n):
                birthdays.append(random.randint(0, 364))
            if has_duplicates(birthdays):
                num_wins += 1
        probabilities.append(num_wins / num_iterations)
    return probabilities

print(f'{simulate_birthday_problem(2000) = }')