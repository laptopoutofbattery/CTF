RSA
-
Some basics on RSA encryption and decryption
### Encryption
1. Choose 2 prime numbers **p** and **q**
2. Calculate **n** through **p * q**
3. Calculate **phi** through **λ(n)** [Carmichael function](https://en.wikipedia.org/wiki/Carmichael%27s_totient_function)
4. Choose a number **e** such that **1<e<λ(n)** and **e** is coprime to **λ(n)**
5. Determine **d** as the **modular multiplicative inverse** of **e** such that **e * d mod λ(n) = 1**
6. Convert the message **M** into an integer **m** using a reversible protocol, then calculate **c** ciphertext through **m^e mod n**  

[Basic Encryption Code](Basic%20RSA%20Encryption.py)

### Decryption
RSA decryption involves **p, q and d**, all components that are kept secret in encryption.  
Hence, an attack is usually required for decryption.  
1. When **p** and **q** are found, compute **phi** (totient) using **(p-1)*(q-1)**
2. Compute **d** using a function like `gmpy2.invert(e, phi)`
3. Solve for plaintext by computing **ciphertext^d mod n**  

[Basic Decryption Code](Basic%20RSA&20Decryption.py)

Of course, factorising **n** is usually improbable, which is why RSA attacks are needed for specific situations.  
The most basic attack would probably be the [cube root attack](https://crypto.stackexchange.com/questions/33561/cube-root-attack-rsa-with-low-exponent), an attack implemented when **p^e** is small.  
<br></br>
  
Some cool resources:  
[RSA wikipedia page](https://en.wikipedia.org/wiki/RSA_(cryptosystem))  
[RsaCtfTool](https://github.com/Ganapati/RsaCtfTool)  
[CryptoHack RSA challenges](https://cryptohack.org/challenges/rsa/)
