# import numpy as np

# array3d = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]])
# # print(array3d)

# array_of_zeroes = np.zeros((2,3))
# # print(array_of_zeroes)

# random_array = np.random.random(100)
# # print(random_array)

import random

def has_duplicates(values):
    for i in range(len(values)):
        for j in range(len(values)):
            if i != j and values[i] == values[j]:
                return True
    return False

def simulate_birthday_paradox(iterations):
    probabilities = []

    for n in range(2, 61):
        num_matches = 0

        for iteration in range(iterations):
            # generate n birthdays
            birthdays = []
            for person in range(n):
                birthdays.append(random.randint(0, 365))

            # check if any birthdays match
            if has_duplicates(birthdays):
                num_matches += 1
        
        probabilities.append(num_matches / iterations)

    return probabilities

prob = simulate_birthday_paradox(5000)
for n in range(len(prob)):
    print(n + 2, prob[n])