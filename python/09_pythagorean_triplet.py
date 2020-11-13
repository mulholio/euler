import math

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def is_pythagorean_tripet(a, b, c):
    return (a ** 2) + (b ** 2) == (c ** 2)


def sums_to_m(arr):
    return arr[0] + arr[1] + arr[2] == 1000


def product(arr):
    return arr[0] * arr[1] * arr[2]


def get_c(a, b):
    return math.sqrt(a ** 2 + b ** 2)


def find_triplets():
    triplets = []
    for a in range(0, 1000):
        for b in range(0, 1000):
            c = get_c(a, b)
            triplets.append([a, b, c])
    return triplets


def find_m():
    maybe_m_arr = filter(
        lambda arr: arr[0] < arr[1] < arr[2],
        filter(
            sums_to_m,
            find_triplets()
        )
    )
    for x in maybe_m_arr:
        print(product(x))


find_m()
