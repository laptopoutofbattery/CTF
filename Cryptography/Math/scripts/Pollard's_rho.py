from math import gcd

# polynomial used
def f(x, n):
    return int((x * x - 1) % n)

"""
Pollard's rho algorithm for factorisation in O(sqrt(n)) time
returns a prime factor of n or -1 if none is found
https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm
"""
def Factor(n):
    x = 2
    y = 2
    d = 1
    
    while d == 1:
        x = f(x, n)
        y = f(f(y, n), n)
        d = gcd(abs(x - y), n)
        
    if d == n:
        return -1
    
    return d

def FullFactor(n):
    primes = []
    new = Factor(n)
    
    if new == -1:
        primes.append(n)
        return primes
        
    if new != -1 and new not in primes:
        primes.append(new)
        primes += FullFactor(n//new)
    
    return primes

print(FullFactor(40))