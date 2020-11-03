def insertion_sort(a):
    work_done = 0
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1

        while i >= 0 and a[i] > key:
            work_done += 1
            a[i + 1] = a[i]
            i -= 1
        
        work_done += 1
        a[i + 1] = key
    print(f'work done = {work_done}')

import random

'''
n     work_done
  100     2650
 1000   256720
10000 24860828

n^2
'''

n = 10000
values = []
for i in range(n):
    values.append(random.randint(1, 100))
insertion_sort(values)
print(values)

