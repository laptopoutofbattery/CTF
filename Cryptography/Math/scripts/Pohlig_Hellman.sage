from sage.all import IntegerModRing, factor, log, crt

# Stolen from https://github.com/Chongsawad/Pohlig-Hellman/blob/master/pohlig.sage

def pohligHellmanPGH(p,g,h):
    # Initialize F as the field of integers modulo p
    F=IntegerModRing(p)
    # Convert g and h to F
    g=F(g)
    h=F(h)
    # Initialize empty lists for G, H, X, and c
    G=[]
    H=[]
    X=[]
    c=[]
    # Factorize p-1 into its prime factors and exponents
    N=factor(p-1)
    # For each factor of p-1, compute G, H, and X, and add them to the respective lists
    for i in range(0,len(N)):
        G.append(g**((p-1)/(N[i][0]**N[i][1])))
        H.append(h**((p-1)/(N[i][0]**N[i][1])))
        X.append(log(H[i],G[i]))
        c.append((X[i],(N[i][0]**N[i][1])))
    # Print the lists G, H, and X for debugging purposes
    print(f"G={G}\nH={H}\nX={X}")

    #Using Chinese Remainder
    # Reverse the order of the list c
    c.reverse()
    # Apply the Chinese Remainder Theorem to compute the final solution
    for i in range(len(c)):
        if len(c) < 2:
            break
        t1=c.pop()
        t2=c.pop()
        r=crt(t1[0],t2[0],t1[1],t2[1])
        m=t1[1]*t2[1]
        c.append((r,m))
    # Return the final solution as the discrete logarithm mod p
    return c[0][0]