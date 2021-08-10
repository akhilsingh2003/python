t=int(input())
for i in range(t):
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    if a[0]>b[0] and a[1]>b[1]:
        print("A")
    elif a[0]>b[0] and a[2]>b[2]:
        print("A")
    elif a[1]>b[1] and a[2]>b[2]:
        print("A")   
    elif a[0]<b[0] and a[1]<b[1]:
        print("B")    
    elif a[0]<b[0] and a[2]<b[2]:
        print("B")
    elif a[1]<b[1] and a[2]<b[2]:
        print("B")    