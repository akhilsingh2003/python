# cook your dish here
for i in range(int(input())):
    a,b=map(int,input().split())
    z=a+b
    n_prob=0
    for j in range(1,7):
        if (j>z):
            n_prob+=1
    probility=n_prob/6
    probility=str(probility)
    if n_prob==0:
        print("0")
    else:    
        print(probility[:8])