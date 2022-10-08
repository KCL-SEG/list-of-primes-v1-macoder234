"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""




from tabnanny import check
def primes(number_of_primes):

    list = []

    i = 1

    currentNumber = 2

    list.append(2)

    while i <= number_of_primes:
        currentNumber = currentNumber + 1
        x = 2
        while x < currentNumber:
            if x == currentNumber:
                list.append(currentNumber)
            elif currentNumber % x:
                break

        i = i + 1

    print(list)
    return list


# while True:
#     try:
#         primes(int(input().split("")))
#     except ValueError:
#         print("Some input could not be converted to a number!")
#     else:
#         break
