from Crypto.PublicKey import RSA
from Crypto.Util import asn1
from base64 import b64decode
from Crypto.Util.number import inverse
from factordb.factordb import FactorDB
import binascii
import gmpy2
import numpy as np
from Crypto.Util.number import long_to_bytes
import math

#n = int(n,16)
#c = int(c,16)

n = 
e = 
c = 
print(n)


#p = 13305920445642931479052386026768222771380761621855384988444870532593667149516790855039939339511449005518331919187137423089741716398131459756144764545564099
#q = 10058207915809023243548813740985545652034313920885958853243504426963692883261645151140676492127644629008467207694442035587685630429540949208099582585439897
#f = FactorDB(n)
#f.connect()
#result = f.get_factor_list()
#print(result)
#p = result[0]
#q = result[1]

#print(result)
#print(int(math.sqrt(n)))
#p = int(math.sqrt(n))
#q = int(math.sqrt(n))

phi = (p-1)*(q-1)
d = int(gmpy2.invert(e, phi))
#print(d)
#print((e*d)%phi)
#d = inverse(e,phi)
#print(d)

#priv_key = RSA.construct((n, e, d))
m = pow(c, d, n)
#print(m)
#print(str(long_to_bytes(m),"utf-8"))
#print(long_to_bytes(m))

#def hex_pair(x):
    #return ('0' * (len(x) % 2)) + x

#m_hex = '{:x}'.format(m)
#m_hex = hex_pair(m_hex)
#msg = binascii.unhexlify(m_hex)
msg = long_to_bytes(m)
print(msg)