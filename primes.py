"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""


def isPrime(currentNumber):
    for x in range(2, currentNumber-1):
        if (currentNumber % x == 0):
            return False
    return True


def primes(number_of_primes):

    list = []

    currentNumber = 2

    while True:
        if (isPrime(currentNumber)):
            list.append(currentNumber)
            if (len(list) == number_of_primes):
                break
        currentNumber += 1

    print(list)
    return list


# while True:
#     try:
#         primes(int(input().split("")))
#     except ValueError:
#         print("Some input could not be converted to a number!")
#     else:
#         break
