import math

a = 66528
b = 52920
##a = 10 #test
##b = 6 #test

if a<b:
    s = b
    b = a
    a = s

gcd=0

if a==0:
    gcd=b
if b==0:
    gcd=a

#a = b*quotient+remainder
q = a//b
r = a-(b*q)
print(math.gcd(b,r))