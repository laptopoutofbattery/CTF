from pwn import *
import string
import random
import sys

dict = string.ascii_lowercase
def decrypt(ct, key):
    pt = ""
    i = 0
    for c in ct:
        if c in dict:
            x = dict[(dict.index(c) - dict.index(key[i%4]) + 26) % 26]
            pt += x
            i += 1
        else: pt += c
        
    return pt

def bruteforce(ct):
    fleg = "}fleg"
    cool = "actf{"
    for l in range(26):
        for q in range(26):
            for t in range(26):
                for p in range(26):
                    key = dict[l]+dict[q]+dict[t]+dict[p]
                    print(key)
                    x = decrypt(ct, key)
                    if cool in x:
                        if fleg in x:
                            print(x)
                            poss = x.index("actf{")
                            pose = x.find("}fleg",poss)
                            pt = x[poss:pose+1]
                            return pt
                        
    # while True:
    #     key = "".join(random.choices(dict, k=4))
    #     print(key)
    #     x = decrypt(ct, key)
    #     if cool in x:
    #         if fleg in x:
    #             print(x)
    #             poss = x.index("actf{")
    #             pose = x.find("}fleg",poss)
    #             pt = x[poss:pose+1]
    #             return pt

if __name__ == "__main__":
    con = remote('challs.actf.co',31333)
    print(con.recvline())
    for i in range(49):
        a = con.recvline()
        print(a)
        C = a.decode('UTF-8')
        if C.find("Nope!") != -1:
            print(C)
            sys.exit()
        if i < 10:
            c = C[13:-1]
        else: c = C[14:-1]
        x = bruteforce(c)
        print(x)
        con.sendline(x)
