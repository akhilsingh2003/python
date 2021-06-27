def even(a):
    return  lambda a : a%2==0
lis=[i for i in range(int(input()))] 
print(even(lis))