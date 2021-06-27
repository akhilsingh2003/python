t = int(input())
for i in range(t):
    n,m=map(int,input().split())
    mod=1000000007
    res=1 
    a=2
    z=n 
    while(z>0):
        if(z%2==1):
            res*=a%(mod)
        a*=a%(mod)
        z=z//2
    res=res%mod
    res-=(1%mod)
    z=m
    a=res
    r=1 
    while(z>0):
        if(z%2==1):
            r*=a%(mod)
        a*=a%(mod)
        z=z//2
    r=r%mod 
    print(r)