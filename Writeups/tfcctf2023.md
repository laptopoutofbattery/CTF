TFC CTF 2023
-

### cypherehpyc
The only challenge i did in this ctf, a pretty standard AES oracle challenge.

```python
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

KEY = b"redacted" * 2

FLAG = "redacted"

initial_cipher = bytes.fromhex(input("Initial HEX: ").strip())

cipher = AES.new(KEY, AES.MODE_ECB).encrypt(pad(initial_cipher, 16))
print(cipher.hex())
cipher = AES.new(KEY, AES.MODE_ECB).encrypt(pad(cipher, 16))
print(cipher.hex())

cipher = AES.new(KEY, AES.MODE_ECB).encrypt(pad(cipher, 16))
result = bytes.fromhex(input("Result HEX: ").strip())

if cipher == result:
    print(FLAG)
else:
    print("Not quite...")
```

We first input a plaintext, which is encrypted using AES ECB, then encrypted again. We are given these two ciphertexts.  
To get the flag, we have to input the correct ciphertext when our plaintext is encrypted thrice.  
The first thing I noticed was that the key was not randomly generated, but is static. I tested this further in the challenge instance:  
![Screenshot](../../assets/images/tfcctforacle.png)  
The ciphertexts are the same when given the same input, which confirms this.  

With that, all we need to do its encrypt the same message once, get the first ciphertext, and input this ciphertext again to be encrypted. After that, the second ciphertext will be our plaintext encrypted 3 times!  
Then, we simply enter the plaintext and input this second ciphertext as the result hex, which gives the flag.