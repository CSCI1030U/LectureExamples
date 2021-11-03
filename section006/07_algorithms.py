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
    op_count = 0

    # for all elements except the first element
    # insert each unsorted element into the sorted portion of the list
    for j in range(1, len(a)):
        # save this value for later (the value to be inserted)
        key = a[j]

        # move all the larger values to the right
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            op_count += 1
            i -= 1
        
        # insert the value into the empty space in the list
        a[i + 1] = key
        op_count += 1
    return op_count

import random 

for n in range(1000, 10001, 1000):
    values = []
    for i in range(n):
        values.append(random.randint(0, 100))

    num_ops = insert_sort(values)
    print(f'the sorted list of {n} elements used {num_ops} operations.')




# coding challenge:  reverse insertion sort (time permitting)

