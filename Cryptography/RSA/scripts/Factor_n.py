#use when n is small enough to be factorised
from factordb.factordb import FactorDB
import gmpy2
from Crypto.Util.number import long_to_bytes

#placeholder values
n = 0
e = 65537
c = 0

f = FactorDB(n)
f.connect()
result = f.get_factor_list()
p = result[0]
q = result[1]

phi = (p-1)*(q-1)
d = int(gmpy2.invert(e, phi))

m = pow(c, d, n)
msg = long_to_bytes(m)
print(msg)