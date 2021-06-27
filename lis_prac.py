t=int(input())
for i in range(t):
    n=int(input())
    for j in range(n*t):
        Q,N=input().split()
        for k in range(n*t):
            if Q[k]!=Q[k+1] and Q[k]!=Q[k+2] and Q[k+1]!=Q[k+2]:
                print(k)


