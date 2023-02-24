from Crypto.PublicKey import RSA

f = open('public.pem','r') #placeholder filename
key = RSA.importKey(f.read())
print(key.n)
print(key.e)