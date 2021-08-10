n = list(input())
n.sort(reverse=True)
x = int("".join(n))
c = 0
while x != 6174:
    x=list(str(x))
    a_sort = sorted(x)
    b_sort = sorted(x,reverse = True)
    a = int("".join(a_sort)) 
    b = int("".join(b_sort))
    x = b - a
    c += 1    
print(c)