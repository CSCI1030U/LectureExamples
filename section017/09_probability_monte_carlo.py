# the birthday paradox

import random 

def has_duplicates(elements):
    for i in range(len(elements)):
        if elements.count(elements[i]) > 1:
            return True 
    return False

# print(has_duplicates([1,2,3,4,2]))

def simulate_birthday_paradox(num_iterations):
    probabilities = []

    for n in range(2, 45):
        num_matches = 0

        for iteration in range(num_iterations):
            birthdays = []
            for person in range(n):
                birthdays.append(random.randint(0, 365))
            
            # check to see if any of the birthdays match
            # if so increase the count (num_matches)
            if has_duplicates(birthdays):
                num_matches += 1
        
        probabilities.append(num_matches / num_iterations)

    return probabilities

prob = simulate_birthday_paradox(2000)
for n in range(len(prob)):
    print(f'For a class of {n + 2}, the probability is {prob[n]}')
    