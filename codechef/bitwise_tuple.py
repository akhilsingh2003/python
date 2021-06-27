t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    x=(2**n-1)%(10**9+7)
    res=x**m % (10**9+7)
    print(res)