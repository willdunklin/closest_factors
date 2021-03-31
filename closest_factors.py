# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %% 
# Here we're trying to get the nearest factors of a number n
# For example, we may want to convert a 1d array of length a
# into the most square 2d matrix possible. This algorithm
# efficiently shows what the dimensions a,b should be for n


# %%
from math import sqrt, ceil

# look for all the squares mod a base
base = 1024
endings = []
for i in range(base):
    e = (i*i)%base
    if e not in endings:
        endings.append(e)


# %%
# check if x is a perfect square, if it is: return its sqrt, otherwise return -1
def perfect_square(x):
    if x % base in endings:
        sqrt_x = int(sqrt(x))
        if sqrt_x * sqrt_x == x:
            return sqrt_x
    return -1


# %%
def fermat(n):
    # not prime factors 
    if n == 0 or n == 1:
        return []

    # wait until n is odd
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # we don't want 1 in the factor list 
    if n == 1:
        return factors

    # now apply fermat's factorization method (https://en.wikipedia.org/wiki/Fermat%27s_factorization_method)
    a = int(ceil(sqrt(n)))
    b2 = a*a - n
    b = perfect_square(b2)
    while b == -1:
        b2 = b2 + 2*a + 1
        a += 1
        b = perfect_square(b2)

    # if this is a prime factor
    if a - b == 1:
        return factors + [a+b]
    
    return factors + fermat(a + b) + fermat(a - b)


# %%
# we want numbers a,b s.t. n = a*b, where we're minimizing |a-b|
def closest_factors(n):
    
    # if n is a perfect square, a-b = 0
    sqrt_n = perfect_square(n) 
    if sqrt_n != -1:
        return (sqrt_n, sqrt_n)
    
    # otherwise use fermat factorization to get prime factors
    prime_factors = fermat(n)
    # sort them in descending order
    prime_factors.sort(reverse=True)

    # now we greedily multiply the largest remaining pf to the smaller of a and b
    a = 1
    b = 1
    for f in prime_factors:
        if b < a:
            b *= f
        else:
            a *= f
    
    return (a, b)


# %%
print(closest_factors(5883219220))
# %%
