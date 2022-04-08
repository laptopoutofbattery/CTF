#implementation of cube root attack, a basic rsa attack when p^e is small
from Crypto.Util.number import long_to_bytes
import gmpy2

#public key
n = #modulus
e = #public exponent (in this case, usually a small number like 3)
c = #ciphertext

#cube root attack
for k in range(1000000):
  if gmpy2.iroot(c + (k * n), e)[1]:
      print(long_to_bytes(gmpy2.iroot(c + (k * n), e)[0]))
