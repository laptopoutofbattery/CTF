Groups and Rings
-

### Groups
A group consists of a set $G$ and a rule, denoted by $\cdot$, for combing two elements $a, b \in G$ to obtain an element $a \cdot b \in G$. The composition operation $\cdot$ is required to have the following three properties:  
- Associative: $(a \cdot b) \cdot c$ = $a \cdot (b \cdot c)$
- Identity: there exists a neutral element $e$ such that $a \cdot e = a$
- Inverse: within the set there's another (unique) element such that $a \cdot a^{-1} = 1$

A commutative group or an abelian group also satisfies:
- Commutative: $a * b = b * a$, $a + b = b + a$

If $G$ has finitely many elements, we say $G$ is a finite group.  
The order of $G$ is the number of elements in $G$, denoted by $|G|$ or #$G$  

Exponentiation can be done by applying the group operation $\cdot$ multiple times, i.e. $g^2 = g \cdot g$, $g^3 = g \cdot g \cdot g$ and so on.

The order of an element $a \in G$ is the smallest possible $d$ such that $a^d = e$, where $e$ is the identity element of $G$. If no such $d$ exists, then $a$ is said to have infinite order.  
If $G$ is a finite group, every element of $G$ has a finite order.  
[Lagrange's Theorem](https://en.wikipedia.org/wiki/Lagrange%27s_theorem_(group_theory)): the order of an element $a \in G$ divides the order $|G|$

### Rings
