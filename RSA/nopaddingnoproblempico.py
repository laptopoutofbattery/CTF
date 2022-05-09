from pwn import *
from Crypto.Util.number import long_to_bytes

con = remote('mercury.picoctf.net', 33780)
n = 0
e = 65537
c = 0
for i in range (7):
    a = con.recvline()
    #print(con.recvline())
    hmm = a.decode('UTF-8')
    if "n:" in hmm:
        print(a)
        n = int(hmm[2:-1])
        print(type(n))
    elif "ciphertext:" in hmm:
        print(a)
        C = [int(i) for i in hmm.split() if i.isdigit()]
        print(type(C))
        c = C[0]
        print(type(c))
con.sendline(str(c+n))
for i in range(3):
    l = con.recvline()
    l = l.decode('UTF-8')
    if "ciphertext" in l:
        C = [int(i) for i in l.split() if i.isdigit()]
        c = C[0]
        print(long_to_bytes(c))
con.sendline()