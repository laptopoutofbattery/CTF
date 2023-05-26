import random
from math import gcd

p = 2**16+1

# LCG to break
class LCG():
    def __init__(self, p):
        self.p = p
        self.X = random.randint(0, p) # seed
        
    def getnext(self):
        self.X = (75 * self.X + 74) % p
        return self.X
    

def main():
    lcg = LCG(p)
    randnumbers = [lcg.getnext() for _ in range(10)] # get 10 random values from LCG
    
    t = [randnumbers[i]-randnumbers[i-1] for i in range(1, len(randnumbers))] # t_n = X_n+1 - X_n
    multiples = [(t[i+2] * t[i] - t[i+1]**2) for i in range(len(t) - 2)] # t_n+2*t_n - (t_n+1)^2
    
    found_p = multiples[0]
    for i in range(1, len(multiples)):
        found_p = gcd(found_p, multiples[i])
    print("p = "+str(found_p))
    
    # X_n+2 - X_n+1 = a(X_n+1 - X_n) mod p
    found_a = (((randnumbers[2] - randnumbers[1]) % found_p) * pow(randnumbers[1] - randnumbers[0], -1, found_p)) % p
    print("a = "+str(found_a))
    
    # c = X_n+1 - aX_n mod p
    found_c = (randnumbers[1] - found_a * randnumbers[0]) % p
    print("c = "+str(found_c))
    

if __name__=='__main__':
    main()