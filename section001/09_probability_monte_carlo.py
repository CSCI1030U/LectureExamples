# the birthday paradox

import random 

def has_duplicates(elements):
    for element in elements:
        if elements.count(element) > 1:
            return True 
    return False

def simulate_birthday_problem(num_iterations):
    probabilities = []

    for n in range(2, 51):
        num_matches = 0
        for iteration in range(num_iterations):
            birthdays = []
            for person in range(n):
                birthdays.append(random.randint(0, 364))
            
            if has_duplicates(birthdays):
                num_matches += 1
    
        probabilities.append(num_matches / num_iterations)
    
    return probabilities

prob = simulate_birthday_problem(2000)
for n in range(len(prob)):
    print(f'For a class of size {n + 2}, the probability is {prob[n]}')