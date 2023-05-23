from gmpy2 import isqrt, sqrt
from math import ceil

# Fermat's Factorisation method
def Factor(n):
    a = ceil(sqrt(n))
    b = a*a-n