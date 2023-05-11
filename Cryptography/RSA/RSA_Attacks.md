RSA Attacks
-
Textbook attacks on RSA

### Factorisation
For smaller $n$ values, factorisation can be used to get $p$ and $q$, usually using http://factordb.com/.
[Script](Factor_n.py)

### Cube Root Attack
When $e$ and $m$ are small, we can bruteforce the modulo as $m^e = C + kn$ where $k$ is a constant. After which we just need to take the $e$th root to get $m$.
[Script](Cube_Root_Attack.py)

### Common Modulus
In the scenario where we have
$$C_1 = m^{e_1} \text{ } (mod \text{ } n)$$
$$C_2 = m^{e_2} \text{ } (mod \text{ } n)$$
We are able to solve for $n$ if $e_1$ and $e_2$ have a gcd of 1.
All we need to do is calculate the bezout coefficients for $e_1$ and $e_2$ such that $e_{1}*u + e_{2}*v = 1$, then take each $C$ to the power of the respective coefficient.
After this, we can multiply them together, giving us
$$C_1 * C_2 = m^{e_{1}*u + e_{2}*v} \text{ } (mod \text{ } n)$$
Which is equal to $m^1$.
[Script](Common_Mod.py)