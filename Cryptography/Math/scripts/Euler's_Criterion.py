# Formula for determining whether an integer is a quadratic residue (has a square root) modulo a prime
# States that Square root of n under modulo p exists if and only if 
# n^{(p-1)/2 % p} = 1

def squareRootExists(n, p):
    if (pow(n, (int)((p - 1) / 2), p) == 1):
        return True
    return False