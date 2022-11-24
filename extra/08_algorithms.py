# exercise 8.3 (fractional knapsack using greedy strategy)
def reverse_insertion_sort_by_value_to_weight(a):
    for j in range(len(a) - 2, -1, -1):
        key = a[j]
        i = j + 1
        while i < len(a) and a[i]['value_to_weight'] > key['value_to_weight']:
            a[i - 1] = a[i]
            i += 1
        a[i - 1] = key

def knapsack_greedy(items_available, weight_limit):
    # calculate the value/weight ratio for all items 
    for item in items_available:
        item['value_to_weight'] = item['value'] / item['weight']

    # sort the items (in descending order) by their value/weight ratio
    reverse_insertion_sort_by_value_to_weight(items_available)

    print(f'{items_available = }')

    # go through the items from greatest value/weight to least, adding items 
    selected_items = []
    available_weight = weight_limit 
    for item in items_available:
        if available_weight == 0:
            break
        elif item['weight'] <= available_weight:
            # take the entire item
            selected_items.append(item)
            available_weight -= item['weight']
        else:
            # take a fraction of the item
            desired_weight = available_weight
            available_weight = 0
            fractional_value = item['value_to_weight'] * desired_weight
            selected_items.append({'name': item['name'], 'weight': desired_weight, 'value': fractional_value})
            break 

    return selected_items

items = [
    {'name': 'Wooden Sculpture', 'weight': 2.0, 'value': 3.5},
    {'name': 'Silver Earrings', 'weight': 1.0, 'value': 150.0},
    {'name': 'Diamond Necklace', 'weight': 1.0, 'value': 750.0},
    {'name': 'Stone Sculpture', 'weight': 45.0, 'value': 8.5},
    {'name': 'Gold Bracelet', 'weight': 5.0, 'value': 275.0},
]
print(f'{knapsack_greedy(items, 8.5) = }')

# exercise 8.4 (fibonacci numbers using dynamic programming)
'''
FIBONACCI-DP(n)
1. solns = [0, 1]
2. if n < 2 then
3.    return solns[n]
4. for i = 2 to n do
5.    append (solns[i-1] + solns[i-2]) to solns
6. return solns[n]
'''
def fib_dp(n):
    if n == 0 or n == 1:
        return n 
    
    solutions = [0, 1]
    for i in range(2, n + 1):
        solutions.append(solutions[i - 1] + solutions[i - 2])

    return solutions[-1]

print(f'{fib_dp(0) = }')
print(f'{fib_dp(1) = }')
print(f'{fib_dp(2) = }')
print(f'{fib_dp(3) = }')
print(f'{fib_dp(4) = }')
print(f'{fib_dp(5) = }')
print(f'{fib_dp(6) = }')
print(f'{fib_dp(7) = }')
print(f'{fib_dp(8) = }')
