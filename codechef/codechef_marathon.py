t=int(input())
for i in range(0,t):
    D,d,A,B,C=map(int,input().split())
    if 1<=D<=10 and 1<=d<=5:
        x=D*d 
        if 1<=x<10:
            print("0")
        elif x==10 :
            print("1")
        elif 10<x<21 or x<42:
            print("2")
        elif x==21:
            print("2")
        