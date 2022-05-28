from Crypto.Util.number import bytes_to_long
import gmpy2

#finding prime numbers and computing n
p = getPrime(512)
q = getPrime(512)
n = p*q

#compute phi and choose e
phi = (p - 1) * (q - 1)
e = 65537 #any number from 1 to phi that is coprime to phi (usually 65537)

#compute d (private key exponent, used for decryption)
d = int(gmpy2.invert(e, phi))

#encrypt plaintext
M = open("pt.txt", "rt").read() #plaintext message
m = bytes_to_long(M)
c = pow(m, e, n)
print(c)
