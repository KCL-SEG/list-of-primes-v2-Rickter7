"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes < 1:
        raise ValueError("The number of primes must be greater than 0")
    list = [2]
    x = 3
    while len(list) < number_of_primes:
        isPrime = True
        for i in range(2, x):
            if x % i == 0:
                prime = False
                break
            i += 1
        if isPrime == True:
            list.append(x)
        x += 1
    return list
