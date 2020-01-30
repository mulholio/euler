# coding: utf-8

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.


def get_primes(n):
    """Gets primes below the given numner"""
    primes = []
    for i in range(1, n):
        print(f"testing {}", n)
        if is_prime(i):
            primes.append(i)
    return primes


def is_prime(n):
    """Returns true if a number is prime"""
    for i in range(1, n):
        print(i)
        if n % i == 0:
            return False
    return True


def sum(ns):
    """Sums all elements of a list"""
    sum = 0
    for n in ns:
        sum += n
    return sum


answer = sum(get_primes(10))
print("answer --------")
print(answer)
