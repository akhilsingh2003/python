t=int(input())
for i in range(t):
    n=int(input())
    lst=[]
    lsts=[]
    lstf=[]
    for i in range(3*n):
        s,n=input().split()
        n=int(n)
        lsts.append(s)
        lst.append(n)
    lsts_set=list(set(lsts))
    for i in range(len(lsts_set)):
        lste=[]
        a=0
        for k in range(len(lst)):
            if lsts_set[i]==lsts[k]:
                lste.append(lst[k])
                a+=lst[k]
        lstf.append(str(a))
    print("".join(sorted(lstf)))            

