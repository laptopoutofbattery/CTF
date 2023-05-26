Linear congruential generator (LCG)
-
LCG is an algorithm for generating pseudo-randomised numbers, defined by:
$$X_{n+1} = (aX_n + c) \mod p$$
Where  
$X$ is the sequence of pseudo-random numbers  
$p$, $0 < p$ is the modulus  
$a$, $0 < a < p$ is the multiplier  
$c$, $0 \le c < p$ is the increment  
and $X_0$ is the seed (starting value)  

To [break a LCG](https://security.stackexchange.com/questions/4268/cracking-a-linear-congruential-generator), we first define a sequence $t$ such that $t_n=X_{n+1}-X_n$.  
Hence $t_n = (aX_n + b) - (aX_{n-1} + b) = at_{n-1} \mod p$, so $t_{n+1} = at_n \mod p$.  
Therefore $t_{n-1} = \frac{t_n}{a} \mod p$, so $t_{n+1}t_{n-1} = (t_n)^2 \mod p$.  
From this we get $t_{n+2}t_n-(t_{n+1})^2 = a^2(t_{n+1}t_{n-1} - (t_n)^2) = 0 \mod p$. So $t_{n+2}t_n-(t_{n+1})^2$ is a multiple of $p$.  
From this if we have many results from a LCG we can get many multiples of $p$. The probability of two random integers being coprime is $\frac{6}{\pi ^2}$%, which also means the probability of the multiples of $p$ sharing no common factors other than $p$ is also $\frac{6}{\pi ^2}$%, and the probability increases with more numbers (note that we are looking at coprime numbers not pairwise coprime).  
We can easily calculate $p$ by taking the gcd of our multiples, and $a$ and $c$ can be solved easily.  
[Script](scripts/LCG_Break.py)  

Another way to break LCG: https://www.srmore.io/posts/breaking-linear-congruential-generator/