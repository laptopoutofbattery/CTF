Modular Arithmetic
-
Used extensively in cryptography, important for understanding encryption algorithms and general math crypto challenges  

### Properties
Taken from https://brilliant.org/wiki/modular-arithmetic/

**Addition**
- If $a+b=c$, then $a+b≡c \mod n$
- If $a≡b \mod n$, then $a+k≡b+k \mod n$ for any integer $k$
- If $a≡b \mod n$ and $c≡d \mod n$, then $a+c≡b+d \mod n$
- If $a≡b \mod n$, then $−a≡−b \mod n$

**Multiplication**
- If $a⋅b=c$, then $a⋅b≡c \mod n$
- If $a≡b \mod n$, then $ka≡kb \mod n$ for any integer $k$
- If $a≡b \mod n$ and $c≡d \mod n$, then $ac≡bd \mod n$

**Exponentiation**
- If $a≡b \mod n$, then $ak≡bk \mod n$ for any positive integer $k$.

**Division**
- If $gcd⁡(k,N)=1$ and $ka≡kb \mod n$, then $a≡b \mod n$

**Multiplicative Inverse**
- The modular multiplicative inverse of an integer $a$ is an integer $x$ with respect to a modulus $n$ such that $ax=1 \mod n$

<br>

### Chinese Remainder Theorem
States that if one knows the remainders of an integer when divided by many coprime moduli, one can find the remainder given when the integer is divided by the product of these moduli.  
More information: https://en.wikipedia.org/wiki/Chinese_remainder_theorem and https://brilliant.org/wiki/chinese-remainder-theorem/  
Script to solve the system of linear congruences: [Chinese_Remainder_Theorem.py](scripts/Chinese_Remainder_Theorem.py)  

<br>

### Fermat's little theorem
If $p$ is a prime numer, the for any integer $a$, $a^p = a \mod p$.  
If $a$ is coprime to $p$ then $a^p-1 = 1 \mod p$.
Extension of Euler's theorem which states $a^{\phi (n)} = 1 \mod n$ where $a$ is coprime to $n$.

<br>

### Useful identities
For calculating inverses when value isn't comprime to modulus:
https://flocto.github.io/writeups/2023/deadsecctf/lcg-writeup/#recovering-the-multiplier
e.g. $a = b^{-1}c \mod p$
let $g = gcd(b, c, p)$
$a = \frac{b^{-1}}{g} \times \frac{c}{g} \mod \frac{m}{g}$