n=int(input("enter the number of rows : "))
a=0
for  i in range(n,0,-1):
    a+=1
    for j in range(1,i+1):
        print(a,end=" ")
    print("\r")