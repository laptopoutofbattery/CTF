a = [91,322,57,124,40,406,272,147,239,285,353,272,77,110,296,262,299,323,255,337,150,102]
msg = ""
for i in range(len(a)):
    a[i] = a[i]%37
    
    if a[i]==0:
        msg+='A'
    elif a[i]==1:
        msg+='B'
    elif a[i]==2:
        msg+='C'
    elif a[i]==3:
        msg+='D'
    elif a[i]==4:
        msg+='E'
    elif a[i]==5:
        msg+='F'
    elif a[i]==6:
        msg+='G'
    elif a[i]==7:
        msg+='H'
    elif a[i]==8:
        msg+='I'
    elif a[i]==9:
        msg+='J'
    elif a[i]==10:
        msg+='K'
    elif a[i]==11:
        msg+='L'
    elif a[i]==12:
        msg+='M'
    elif a[i]==13:
        msg+='N'
    elif a[i]==14:
        msg+='O'
    elif a[i]==15:
        msg+='P'
    elif a[i]==16:
        msg+='Q'
    elif a[i]==17:
        msg+='R'
    elif a[i]==18:
        msg+='S'
    elif a[i]==19:
        msg+='T'
    elif a[i]==20:
        msg+='U'
    elif a[i]==21:
        msg+='V'
    elif a[i]==22:
        msg+='W'
    elif a[i]==23:
        msg+='X'
    elif a[i]==24:
        msg+='Y'
    elif a[i]==25:
        msg+='Z'
    elif a[i]==26:
        msg+='0'
    elif a[i]==27:
        msg+='1'
    elif a[i]==28:
        msg+='2'
    elif a[i]==29:
        msg+='3'
    elif a[i]==30:
        msg+='4'
    elif a[i]==31:
        msg+='5'
    elif a[i]==32:
        msg+='6'
    elif a[i]==33:
        msg+='7'
    elif a[i]==34:
        msg+='8'
    elif a[i]==35:
        msg+='9'
    elif a[i]==36:
        msg+='_'
        
print("picoCTF{",msg,"}")