def factorial(n):
    # factorial(5) => 5 * 4 * 3 * 2 * 1   or  1 * 2 * 3 * 4 * 5 
    result = 1

    # for i in range(1, n + 1):
    #     result = result * i 

    multiplier = n
    while multiplier > 0:
        result *= multiplier
        multiplier -= 1

    # print(name) # yuck!  bad coding practice - don't access global variables in a function
    # instead, pass it as an argument (best practice)

    return result

def main():
    name = 'Randy'
    print(factorial(6))
    multiplier = 7
    print(name)
    print(multiplier)

main()