def insertion_sort(a):
    work_done = 0
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            work_done += 1
            i -= 1 
        a[i + 1] = key
        work_done += 1
    print(work_done)

def reverse_insertion_sort(a):
    for j in range(len(a) - 2, -1, -1):
        key = a[j]
        i = j + 1

        while i < len(a) and a[i] < key:
            a[i - 1] = a[i]
            i += 1
        a[i - 1] = key

'''
n  work_done
------------
100       2483
1000    258223
10000 24653810

n^2
'''

import random
n = 10000
values = []
for i in range(n):
    values.append(random.randint(0, 100))
print(values)
insertion_sort(values)
print(values)

