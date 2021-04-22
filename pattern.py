'''ht = int(input('enter the height'))
pos = int(input('enter the position '))
k = 0
for i in range(1, ht+1):
    print(' '*(ht - i), end='')
    while k != 2*i-1:
        if k == 0 or k == 2*i-2:
            print('*', end='')
        elif i == pos:
            print('*', end='')
        else:
            print(' ', end='')
        k += 1
    k = 0
    print()'''
      
h = int(input())
for i in range(1, h+1):
    print(' '*(h-i)+'*'*(2*i-1))