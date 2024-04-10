"""
    Check if a given number is prime.

    :param n: the number to check for primality
    :return: True if the number is prime, False otherwise
"""
def isPrime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True


nums = range(1,1000)
print(list(filter(isPrime,nums)))
