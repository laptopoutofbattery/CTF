from factordb.factordb import FactorDB
import gmpy2
from Crypto.Util.number import long_to_bytes

#public key
e = #public exponent (usually 65537)
n = #modulus
c = #ciphertext

#use factordb to find p and q (will not work for huge n values)
f = FactorDB(n)
f.connect()
factor_n_list = f.get_factor_list()
p = factor_n_list[0]
q = factor_n_list[1]

#find the totient, private exponent and decrypt the message
phi = (p-1)*(q-1)
d = int(gmpy2.invert(e, phi))
m = pow(c, d, n)
M = long_to_bytes(m)
print(M)

