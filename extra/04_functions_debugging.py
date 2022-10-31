def print_n_times(n, message):
    # base case 
    if n == 0:
        return

    # recursive case
    print(message)
    print_n_times(n - 1, message)

print_n_times(5, 'Hello again!')

def infinite(count):
    print('Hello there!')
    infinite(count + 1)

# infinite(0)