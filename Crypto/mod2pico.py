import gmpy2

a = [104,85,69,354,344,50,149,65,187,420,77,127,385,318,133,72,206,236,206,83,342,206,370]
msg = ""
for i in range(len(a)):
    l = a[i]
    a[i] = a[i]%41
    a[i] = int(gmpy2.invert(a[i], 41))
    
    if a[i]==1:
        msg+='A'
    elif a[i]==2:
        msg+='B'
    elif a[i]==3:
        msg+='C'
    elif a[i]==4:
        msg+='D'
    elif a[i]==5:
        msg+='E'
    elif a[i]==6:
        msg+='F'
    elif a[i]==7:
        msg+='G'
    elif a[i]==8:
        msg+='H'
    elif a[i]==9:
        msg+='I'
    elif a[i]==10:
        msg+='J'
    elif a[i]==11:
        msg+='K'
    elif a[i]==12:
        msg+='L'
    elif a[i]==13:
        msg+='M'
    elif a[i]==14:
        msg+='N'
    elif a[i]==15:
        msg+='O'
    elif a[i]==16:
        msg+='P'
    elif a[i]==17:
        msg+='Q'
    elif a[i]==18:
        msg+='R'
    elif a[i]==19:
        msg+='S'
    elif a[i]==20:
        msg+='T'
    elif a[i]==21:
        msg+='U'
    elif a[i]==22:
        msg+='V'
    elif a[i]==23:
        msg+='W'
    elif a[i]==24:
        msg+='X'
    elif a[i]==25:
        msg+='Y'
    elif a[i]==26:
        msg+='Z'
    elif a[i]==27:
        msg+='0'
    elif a[i]==28:
        msg+='1'
    elif a[i]==29:
        msg+='2'
    elif a[i]==30:
        msg+='3'
    elif a[i]==31:
        msg+='4'
    elif a[i]==32:
        msg+='5'
    elif a[i]==33:
        msg+='6'
    elif a[i]==34:
        msg+='7'
    elif a[i]==35:
        msg+='8'
    elif a[i]==36:
        msg+='9'
    elif a[i]==37:
        msg+='_'
        
print("picoCTF{%s}" % "".join(msg))
