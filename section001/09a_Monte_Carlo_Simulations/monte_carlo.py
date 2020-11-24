# import numpy as np

# a1 = np.array([1.2, 2.1, -0.5, 7.0])
# a2 = np.zeros((8,))
# a3 = np.random.random((10,5))

import random

def check_for_duplicates(elements):
    for i in range(len(elements)):
        for j in range(len(elements)):
            if i != j and elements[i] == elements[j]:
                return True
    return False

def simulate_birthday_paradox(iterations):
    probabilities = []

    for n in range(2, 64):
        num_matches = 0
        for iteration in range(iterations):
            # determine everyone's birthday
            birthdays = []
            for person in range(n):
                birthdays.append(random.randint(0, 365))
            
            # check if we have a match
            if check_for_duplicates(birthdays):
                num_matches += 1
        
        probabilities.append(num_matches / iterations)

    return probabilities

prob = simulate_birthday_paradox(2000)
for n in range(len(prob)):
    print(n + 2, prob[n])
