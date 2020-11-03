def insertion_sort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i -= 1 
        a[i + 1] = key

values = [13,-2,5,11,22,-18,6,-3,4]
insertion_sort(values)
print(values)