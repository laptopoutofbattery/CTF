from math import ceil, sqrt
from gmpy2 import is_square, invert, isqrt
from Crypto.Util.number import long_to_bytes

"""
Fermat's Factorisation method
Based on the representation of an odd integer as the difference of 2 squares
n = a^2 - b^2
  = (a + b)(a - b)
"""

def Factor(n):
    a = isqrt(n) # largest integer where a*a<=n
    if a * a == n:
        return a, a
    a += 1 # ceil(sqrt(n))
    b = a*a-n
    
    while not is_square(b):
        a += 1
        b = a*a-n
        
    return a - isqrt(b), a + isqrt(b)

# placeholder values
n = 0
e = 65537
c = 0

p, q = Factor(n)

phi = (p-1)*(q-1)
d = int(invert(e, phi))

m = pow(c, d, n)
msg = long_to_bytes(m)
print(msg)