"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""


def isPrime(n):
    for i in range(2, n-1):
        if (n % i == 0):
            return False
    return True


def primes(number_of_primes):

    list = []

    while True:
        if (isPrime(i)):
            list.append(i)
            if (len(list) == number_of_primes):
                break
        i += 1

    print(list)
    return list


# while True:
#     try:
#         primes(int(input().split("")))
#     except ValueError:
#         print("Some input could not be converted to a number!")
#     else:
#         break
