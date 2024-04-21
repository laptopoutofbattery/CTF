AmateursCTF 2024
-
I didn't have much time these few days and only managed to attempt one challenge from this ctf, `unsuspicous-rsa`. It was an interesting challenge, so heres the writeup

### unsuspicous-rsa
This challenge is a typical RSA challenge, where `n`, `e` and `c` are given, as well as some source code:
```python
from Crypto.Util.number import *

def nextPrime(p, n):
    p += (n - p) % n
    p += 1
    iters = 0
    while not isPrime(p):
        p += n
    return p

def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1) * n


flag = bytes_to_long(open('flag.txt', 'rb').read().strip())
p = getPrime(512)
q = nextPrime(p, factorial(90))
N = p * q
e = 65537
c = pow(flag, e, N)
print(N, e, c)
```
```
n = 172391551927761576067659307357620721422739678820495774305873584621252712399496576196263035396006999836369799931266873378023097609967946749267124740589901094349829053978388042817025552765214268699484300142561454883219890142913389461801693414623922253012031301348707811702687094437054617108593289186399175149061
e = 65537
c = 128185847052386409377183184214572579042527531775256727031562496105460578259228314918798269412725873626743107842431605023962700973103340370786679287012472752872015208333991822872782385473020628386447897357839507808287989016150724816091476582807745318701830009449343823207792128099226593723498556813015444306241
```
When I first looked at the encryption, fermat's attack came to mind since `nextPrime` is used to get `q`. However, a custom `nextPrime` function is used, and the difference between `p` and `q` is too large to factorise `n` using fermat's factorisation method.  

Let's take a look at the `nextPrime` function:
```python
def nextPrime(p, n):
    p += (n - p) % n
    p += 1
    iters = 0
    while not isPrime(p):
        p += n
    return p
```
1. `(n - p) % n` is added to `p`. This "rounds up" `p` to the next multiple of `n`. For example, if `p` is 7 and `n` is 3, 2 will be added to `p` to make it 9.  
2. 1 is added to `p` such that `p = 1 (mod n)`. In other words, `p = kn + 1` where `k` is some constant.  
3. `n` is continuously added to `p` until `p` is a prime. This means that `p` is still equal to `1 (mod n)`.  

So we know that `q = 1 (mod 90!)`. We can let `p = a (mod 90!)` where `a` is some constant. That aslo means that `p = k(90!) + a` where `k` is another constant.  

We can walkthrough the steps of `nextPrime` to get a more useful equation for `q`:
1. After the first step of `nextPrime`, `q = (k+1)(90!)`
2. Then, `q = (k+1)(90!) + 1`
3. Finally, `q = (k+1)(90!) + b(90!) + 1 = (k+b+1)(90!) + 1` where `b` is some constant

#### The Attack

Now, we can express `n` with these equations:
`n = p*q = (k(90!) + a)*((k+b+1)(90!) + 1) = k(k+b+1)(90!)^2 + k(90!) + a(k+b+1)(90!) + a`
Notice anything about this definition of `n`?  
All of the terms are multiples of 90! except for `a`. Therefore, `n = a (mod 90!)`. This means we can calculate `a`.  

We can continue expanding `n`:  
`n = k(k+b+1)(90!)^2 + k(90!) + a(k+b+1)(90!) + a = k^2(90!)^2 + k((b + 1)(90!)^2 + 90! + a(90!)) + a(b+1)(90!) + a`  
Notice that we have made a quadratic equation in k:
`k^2(90!)^2 + k((b + 1)(90!)^2 + 90! + a(90!)) + a(b+1)(90!) + a - n = 0`  
We already know `a` and `n`, so all we need is `b` and we can find the value of `k` through the qudratic formula.  

The value of `b` is the number of times we add 90! to `q` such that it becomes a prime.  
Remember how `p = 1 (mod 90!)`? This means that all the numbers from 2 to 90 won't be factors of `q`. That suggests that the value of `b` is small, as the factors of `q` must be large. We can confirm this by testing:
```python
from Crypto.Util.number import *

def nextPrime(p, n):
    p += (n - p) % n
    p += 1
    iters = 0
    while not isPrime(p):
        iters += 1
        p += n
    print(iters)
    return p

def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1) * n

p = getPrime(512)
q = nextPrime(p, factorial(90))
```
We use the `iters` variable that was already in the source code. After running this a couple of times, the values seem to all be < 200.  

So we know that `b` is very small. This means we can bruteforce `b` and solve for `k` using the qudratic formula. Once we know `b` and `k`, we can calculate `p` and `q`. Here is the code I used to solve this (code for quadratic solving was from a previous challenge):  
```python
from Crypto.Util.number import *

n = 172391551927761576067659307357620721422739678820495774305873584621252712399496576196263035396006999836369799931266873378023097609967946749267124740589901094349829053978388042817025552765214268699484300142561454883219890142913389461801693414623922253012031301348707811702687094437054617108593289186399175149061
e = 65537
c = 128185847052386409377183184214572579042527531775256727031562496105460578259228314918798269412725873626743107842431605023962700973103340370786679287012472752872015208333991822872782385473020628386447897357839507808287989016150724816091476582807745318701830009449343823207792128099226593723498556813015444306241

def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1) * n

# code stolen from somewhere
def nthroot(x, n):
    # Start with some reasonable bounds around the nth root.
    upper_bound = 1
    while upper_bound ** n <= x:
        upper_bound *= 2
    lower_bound = upper_bound // 2
    # Keep searching for a better result as long as the bounds make sense.
    while lower_bound < upper_bound:
        mid = (lower_bound + upper_bound) // 2
        mid_nth = mid ** n
        if lower_bound < mid and mid_nth < x:
            lower_bound = mid
        elif upper_bound > mid and mid_nth > x:
            upper_bound = mid
        else:
            # Found perfect nth root.
            return mid
    return mid + 1

def quad(_a, _b):
    
    a = factorial(90)**2
    b = factorial(90) * ((_b+1)*factorial(90) + 1 + _a)
    c = _a * ((_b+1)*factorial(90) + 1) - n
    
    d = (b*b) - (4*a*c)
    droot = nthroot(d, 2)
    if droot**2!=d:
        return -1
    if (droot-b)%(2*a)!=0:
        return -1
    
    ptest = (-b+droot)//(2*a)
    return ptest

def brute():
    
    _a = n % factorial(90)
    for _b in range(1, 500):
        k = quad(_a, _b) #_a and _b are a and b from the equation
        if k != -1:
            # print(k)
            # print(x)
            return k, _b
    
    return 0, 0
            
k, _b = brute()
p = k * factorial(90) + (n % factorial(90))
q = (k+1+_b) * factorial(90) + 1
assert p*q == n

phi = (p-1)*(q-1)
d = pow(e, -1, phi)

m = pow(c, d, n)
msg = long_to_bytes(m)
print(msg)
```

We get the flag `amateursCTF{here's_the_flag_you_requested.}`

After the CTF, I saw a solution on discord that used fermat to solve by bruteforcing the difference between `p` and `q` (again, because `b` is small), which was probably the intended solution. But hey I still solved it :)
