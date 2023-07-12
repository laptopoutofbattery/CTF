CrewCTF 2023
-

### matrixrsa
This challenge requires us to exploit an orcale with a custom RSA encryption using matrix exponentiation:  
```python
import os
import random
from Crypto.Util.number import getPrime, long_to_bytes, bytes_to_long
from sympy.polys.matrices import DomainMatrix
from sympy import FiniteField

# secret import
from secret import decrypt
from flag import FLAG


size = 1024//8
e = 65537


def pad(data, length):
    if len(data) >= length:
        raise ValueError("length of data is too large.")
    pad_data = bytes([random.randint(1, 255) for _ in range(length - len(data) - 1)])
    return pad_data + b'\x00' + data


def unpad(paddeddata):
    if b'\x00' not in paddeddata:
        raise ValueError("padding is incorrect.")
    return paddeddata[paddeddata.index(b'\x00')+1:]


def keygen():
    p, q = getPrime(8*size), getPrime(8*size)
    n = p*q
    return ((p, q), n)


def encrypt(msgint, n):
    a = bytes_to_long(os.urandom(int(2*size-1)))
    # sympy.FiniteField treats non-prime modulus instance as Z/nZ
    Zmodn = FiniteField(n)
    mat = DomainMatrix([
            [Zmodn(a), Zmodn(msgint)],
            [Zmodn(0), Zmodn(a)]
        ], (2, 2), Zmodn)

    enc = mat**int(e)
    enc_0 = int(enc[0,0].element.val)
    enc_1 = int(enc[0,1].element.val)
    return (enc_0, enc_1)


def main():
    try:
        banner = "Welcome to matrix RSA world"
        print(banner)

        (p,q), n = keygen()

        paddedflag = pad(FLAG, 2*size-1)
        assert unpad(paddedflag) == FLAG
        paddedflagint = bytes_to_long(paddedflag)
        encflag_0, encflag_1 = encrypt(paddedflagint, n)
        assert decrypt((encflag_0, encflag_1), (p, q)) == paddedflagint
        print("Here is encrypted flag(enc_0, enc_1):")
        print(long_to_bytes(encflag_0).hex())
        print(long_to_bytes(encflag_1).hex())

        while True:
            print("Please input encrypted message(enc_0, enc_1):")
            enc_0 = bytes_to_long(bytes.fromhex(input('>> ')))
            enc_1 = bytes_to_long(bytes.fromhex(input('>> ')))
            if enc_0 >= n or enc_1 >= n:
                print("size error")
                continue
            if (enc_0 * encflag_1 - enc_1 * encflag_0) % n == 0:
                print("Do not input related to encrypted flag")
                continue
            dec = decrypt((enc_0, enc_1), (p, q))
            if FLAG in long_to_bytes(dec):
                print("Do not input encrypted flag")
            else:
                print("Here is decrypted message:")
                print(long_to_bytes(int(dec)).hex())
    except:
        quit()


if __name__ == "__main__":
    main()
```
We observe that the encrypt function constructs a matrix of `[a, msg], [0, a]`, then performs matrix exponentiation to the power of `e` (65537) modulo `n`, similar to regular RSA encryption. To understand what the encryption process actually does, I first experimented exponentiation with smaller powers.  
When we square the matrix, we get `[a^2, 2*a*msg], [0, a^2]`  
When we cube the matrix, we get `[a^3, 3*(a^2)*msg], [0, a^3]`  
Clearly theres a pattern, allowing us to deduce that the final result of encryption is `[a^65537, 65537*(a^65536)*msg], [0, a^65537]`.  
Thus, we know that `decrypt` takes in `a^65537` and `65537*(a^65536)*msg`, takes the first variable to the power of `65537^-1` to get `a`, then divides the second variable by `65537*(a^65536)` to get `msg`.  
The oracle gives us these two values, but checks whether the flag is in the decrypted message, so we can't directly input them to retrieve it. However if we were to add a constant value to the ciphertext and decrypt it, we can just deduct the value later to retrieve the flag.  
If we were to add 1 to the ciphertext and input `a^65537` normally, our result is `msg + 1/(65537*(a^65536))`. We can easily find the value of our constant by inputting `a^65537` and 1 into the oracle and getting the result from decryption.  
Solution:  
```python
from Crypto.Util.number import long_to_bytes
from pwn import *

conn = remote('matrixrsa.chal.crewc.tf', 20001)
def send(y):
    h = hex(y)[2:]
    pad = len(h) + len(h)%2
    conn.sendline(h.zfill(pad).encode())

conn.recvuntil(b'Here is encrypted flag(enc_0, enc_1):\n')
a_0 = int(conn.recvline().decode()[:-1], 16)
c = int(conn.recvline().decode()[:-1], 16)
conn.recv()

send(a_0)
conn.recv()
send(1)
conn.recvuntil(b'Here is decrypted message:\n')
a_1 = int(conn.recvline().decode()[:-1], 16)
conn.recv()

send(a_0)
conn.recv()
send(c+1)
conn.recvuntil(b'Here is decrypted message:\n')
m = int(conn.recvline().decode()[:-1], 16)

conn.close()

print(long_to_bytes(m-a_1))
```

<br>

### matrixrsa2
Same challenge as above, but the matrix is edited slightly:  
```python
mat = DomainMatrix([
        [Zmodn(a), Zmodn(msgint) - Zmodn(a) ** 0x1337 - Zmodn(0xdeadbeef)],
        [Zmodn(0), Zmodn(a)]
    ], (2, 2), Zmodn)
```
This time, instead of `65537*(a^65536)*msg`, the encryption gives `65537*(a^65536)*(msg-a^A-B)` where `A` and `B` are the above constants. As such, when we try to decrypt `1` again, we instead get `1/(65537*(a^65536)) + a^A + B`. This seems to prevent the same exploit, but we can obtain the value of `a^A + B` easily by decrypting 0.
Solution:  
```python
from Crypto.Util.number import long_to_bytes
from pwn import *

conn = remote('matrixrsa2.chal.crewc.tf', 20002)
def send(y):
    h = hex(y)[2:]
    pad = len(h) + len(h)%2
    conn.sendline(h.zfill(pad).encode())

conn.recvuntil(b'Here is encrypted flag(enc_0, enc_1):\n')
a_0 = int(conn.recvline().decode()[:-1], 16)
c = int(conn.recvline().decode()[:-1], 16)
conn.recv()

send(a_0)
conn.recv()
send(1)
conn.recvuntil(b'Here is decrypted message:\n')
a_1 = int(conn.recvline().decode()[:-1], 16)
conn.recv()

send(a_0)
conn.recv()
send(0)
conn.recvuntil(b'Here is decrypted message:\n')
a_2 = int(conn.recvline().decode()[:-1], 16)
conn.recv()

send(a_0)
conn.recv()
send(c+1)
conn.recvuntil(b'Here is decrypted message:\n')
m = int(conn.recvline().decode()[:-1], 16)

conn.close()

print(long_to_bytes(m-(a_1-a_2)))
```