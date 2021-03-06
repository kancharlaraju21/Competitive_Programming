def power(a,b):
    res=1
    while b>0:
        if b&1:
            res=res*a
        a=a*a
        b=b>>1
    return res

def power_mod(a,b,m):
    a%=m
    res=1
    while b>0:
        if b&1:
            res=(res*a)%m
        a=(a*a)%m
        b=b>>1
    return res
    
while True:
    try:
        b = input()
        if b == "":
            b = int(input())
        else:
            b = int(b)
        p = int(input())
        m = int(input())
    except EOFError:
        break
    print(power_mod(b, p, m))