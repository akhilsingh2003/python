n=int(input("enter the number of rows :"))

for i in range(n, 0, -1):

    num = i

    for j in range(0, i):

        print(num, end=" ")

    print("\r")