Finite Fields
-
aka Galois Fields, fields with a finite number of elements under two operations and a set of properties  

### Properties
Each finite field $\mathbb{F}_{p^m}$ has $p^m$ elements for a prime $p$ and positive integer $m \ge 1$.  
There exist no finite fields with $q$ elements if $q$ is not a prime power.  
When $m = 1$, we get a prime field. When $m > 1$, we get an extension field.  

Finite fields have the following properties (similar to groups):  
- Closed: any operation performed with elements from the set returns an element contained in the original set
- Associative: $(a * b) * c$ = $a * (b * c)$, $(a + b) + c$ = $a + (b + c)$
- Identity: there exists a neitral element $b$ usually 1 such that $a * b = a$
- Inverse: within the set there's another element such that $a * a^{-1} = 1$
- Commutative: $a * b = b * a$, $a + b = b + a$

### Prime fields
The integers modulo $p$ form a prime field $\mathbb{F}_{p}$ under mod $p$ addition and multiplication.  
All operations in prime fields are done modulo $p$.  

### Extension fields
Elements of extension fields ($\mathbb{F}_{p^m}$ where $m > 1$) are polynomials, taking the form of $a _{m-1}X^{m-1} + \text{...} + a_1X^1 + a_0$.
