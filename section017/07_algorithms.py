# coding exercise:  insertion sort, operation analysis

# INSERT-SORT(A)
# 1  for j = 2 to length[A] do
# 2     key = A[j]
# 3     i = j-1
# 4     while i > 0 and A[i] > key do
# 5        A[i+1] = A[i]
# 6        i = i-1
# 7     A[i+1] = key

def insert_sort(a):
    # for every unsorted element
    # j - index of the next element to be inserted
    for j in range(1, len(a)):
        # make a copy of the current value to be inserted
        key = a[j]

        # moves all of the larger elements in the sorted list to the right
        i = j - 1
        while i >= 0 and a[i] > key:
            # move the element to the right
            a[i + 1] = a[i]

            # move the index to the next element (to the left)
            i -= 1
        
        # insert the element into the empty space
        a[i + 1] = key

test_list = [3,-2,11,-16,5,9,16,4]
insert_sort(test_list)
# print(test_list)

# coding challenge:  reverse insertion sort (time permitting)

def reverse_insert_sort(a):
    # forward insert sort goes from 1..len(a)-1
    # reverse insert sort goes from len(a)-2..0
    for j in range(len(a) - 2, -1, -1):
        key = a[j]

        i = j + 1
        while i < len(a) and a[i] < key:
            a[i - 1] = a[i]
            i += 1
        a[i - 1] = key

test_list = [3,-2,11,-16,5,9,16,4]
reverse_insert_sort(test_list)
print(test_list)

# extra code - counting the operations
def insert_sort_with_counting(a):
    op_count = 0

    # for every unsorted element
    # j - index of the next element to be inserted
    for j in range(1, len(a)):
        # make a copy of the current value to be inserted
        key = a[j]

        # moves all of the larger elements in the sorted list to the right
        i = j - 1
        while i >= 0 and a[i] > key:
            # move the element to the right
            a[i + 1] = a[i]
            op_count += 1

            # move the index to the next element (to the left)
            i -= 1
        
        # insert the element into the empty space
        a[i + 1] = key
        op_count += 1

    return op_count

import random 

for n in range(1000, 10001, 1000):
    values = []
    for i in range(n):
        values.append(random.randint(0, 100))
    num_ops = insert_sort_with_counting(values)
    print(f'sorting a list with {n} elements takes {num_ops} operations')