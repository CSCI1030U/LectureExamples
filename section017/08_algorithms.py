# exercise 8.1 (reverse insertion sort)
'''
INSERT-SORT(A)
1  for j = 2 to length[A] do
2     key = A[j]
3     i = j-1
4     while i > 0 and A[i] > key do
5        A[i+1] = A[i]
6        i = i-1
7     A[i+1] = key
'''
def reverse_insertion_sort(a):
    for j in range(len(a) - 2, -1, -1):
        key = a[j]
        i = j + 1
        while i < len(a) and a[i] < key:
            a[i - 1] = a[i]
            i += 1
        a[i - 1] = key       

# values = [5,2,1,4,3]
# values = [1,2,3,4,5]
# values = [5,4,3,2,1]
# values = [5]
values = []
reverse_insertion_sort(values)
print(f'{values = }')

# exercise 8.2 (search list using divide and conquer)
def search_dc(values, to_find):
    # base cases
    if len(values) == 0:
        return False

    if len(values) == 1:
        return to_find == values[0]

    # divide 
    middle = len(values) // 2
    a = values[:middle]
    b = values[middle:]

    # conquer 
    found_in_first_half = search_dc(a, to_find)
    found_in_second_half = search_dc(b, to_find)

    # combine
    return found_in_first_half or found_in_second_half

print(f'{search_dc([5,2,1,4,3], 1) = }')
print(f'{search_dc([5,2,1,4,3], 3) = }')
print(f'{search_dc([5,2,1,4,3], 5) = }')
print(f'{search_dc([5,2,1,4,3], 0) = }')

# exercise 8.3 (fractional knapsack using greedy strategy)
def reverse_insertion_sort_tuple_by_fourth(a):
    for j in range(len(a) - 2, -1, -1):
        key = a[j]
        i = j + 1
        while i < len(a) and a[i][3] > key[3]:
            a[i - 1] = a[i]
            i += 1
        a[i - 1] = key

def knapsack_greedy(items_available, max_weight):
    # calculate the value/weight ratio of all items 
    value_to_weight = []
    for item in items_available:
        value_to_weight.append((item[0], item[1], item[2], item[2]/item[1]))

    # sort the items by their ratio (descending)
    reverse_insertion_sort_tuple_by_fourth(value_to_weight)

    # one at a time, choose items in ratio order
    available_weight = max_weight
    selected_items = []
    for item in value_to_weight:
        if item[1] < available_weight:
            # take the entire item 
            selected_items.append(item)
            available_weight -= item[1]
        else:
            desired_weight = available_weight
            fractional_value = item[3] * desired_weight
            selected_items.append((item[0], desired_weight, fractional_value, item[3]))
            available_weight = 0
            break 
    return selected_items

items = [
    # name, weight, value
    ('Wooden Sculpture', 2.0, 3.5),
    ('Silver Earrings', 1.0, 150.0),
    ('Diamond Necklace', 1.0, 750.0),
    ('Stone Statue', 45.0, 8.5),
    ('Gold Bracelet', 5.0, 275.0)
]
print(f'{knapsack_greedy(items, 8.5) = }')

# exercise 8.4 (fibonacci numbers using dynamic programming)
def fib_dp(n):
    if n == 0 or n == 1:
        return n 
    
    solutions = [0, 1]
    for n in range(2, n + 1):
        solutions.append(solutions[n - 1] + solutions[n - 2])
    
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
