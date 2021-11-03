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

    # goes from the 2nd element to the end of the list
    # inserts each unsorted element into the sorted part of the list, one at a time
    for j in range(1, len(a)):
        # make a copy of the value to be inserted (outside of the list)
        key = a[j]

        # move all larger elements (to the left of j) right one space
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            op_count += 1
            i -= 1

        # insert the value into the newly positioned hole in the list
        a[i + 1] = key
        op_count += 1
    
    return op_count

import random

# n = 1000, 2000, 3000, 4000, ..., 10000
for n in range(1000, 10001, 1000):
    values = []
    for i in range(n):
        values.append(random.randint(0, 100))
    num_ops = insert_sort(values)
    print(f'For a list of length {n}, we did {num_ops} operations.')

# coding challenge:  reverse insertion sort (time permitting)

