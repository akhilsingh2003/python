x = int(input())
y = int(input())
z = int(input())
permu = []
for i in range(1,x+1):
    for j in range(1,y+1):
        for k in range(1,z+1):
                permu.append([i, j, k])
print(permu)