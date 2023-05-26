RSA Attacks
-
Textbook attacks on RSA, most can be solved using [RsaCtfTool](https://github.com/RsaCtfTool/RsaCtfTool)  

### Factorisation
For smaller $n$ values, factorisation can be used to get $p$ and $q$, usually using http://factordb.com/.  
When small primes are used to generate $n$, [Pollard's rho algorithm](https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm) ($O(\sqrt n)$ time complexity) or [elliptic-curve factorisation (ecm)](https://en.wikipedia.org/wiki/Lenstra_elliptic-curve_factorization) can be used to factorise $n$.  
Use `ecm.factor(n)` in [SageMath](https://doc.sagemath.org/html/en/reference/interfaces/sage/interfaces/ecm.html) for elliptic curve factorisation.  
[Script (using Factordb)](scripts/Factor_n.py)

<br>

### Cube Root attack
When $e$ and $m$ are small, we can bruteforce the modulo as $m^e = C + kn$ where $k$ is a constant. After which we just need to take the $e$th root to get $m$.  
[Script](scripts/Cube_Root_Attack.py)

<br>

### Common Modulus
In the scenario where we have  

<p align="center">
  <img src="../../assets/images/CommonMod.svg">
</p>  

We are able to solve for $n$ if $e_1$ and $e_2$ have a gcd of 1.
All we need to do is calculate the bezout coefficients for $e_1$ and $e_2$ such that $e_{1}*u + e_{2}*v = 1$, then take each $C$ to the power of the respective coefficient.
After this, we can multiply them together, giving us
$$C_1 * C_2 = m^{e_{1}*u + e_{2}*v} \mod n$$
Which is equal to $m^1$.  
[Script](scripts/Common_Mod.py)

<br>

### Fermat's attack
When $p$ and $q$ are close ($p-q < n^{\frac{1}{4}}$), [Fermat's factorization method](https://en.wikipedia.org/wiki/Fermat%27s_factorization_method) can be used to factorise $n$.  
We do this by expressing $n$ as $(a-b)(a+b)$.  
[Script](scripts/Fermat_Attack.py)

<br>

### Hastad's Broadcast attack
When we have

<p align="center">
  <img src="../../assets/images/Hastad.svg">
</p>  

we can use the Chinese Remainder Theorem to construct a solution for $m^3$ and from there obtain $m$ through cube root.
[Script](scripts/Hastad.py)

<br>

### Wiener's attack
If $e$ is relatively big compared to $n$, then $d$ is probably small. In this case Wiener's attack can be used, specifically when $d < \frac{1}{3}n^{\frac{1}{4}}$.  
The math behind the theorem is too long to put here but this [post](https://bitsdeep.com/posts/attacking-rsa-for-fun-and-ctf-points-part-2/) covers it pretty well.  
[Script using a module (note that RsaCtfTool should work as well)](scripts/Wiener.py)