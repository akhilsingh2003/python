n=int(input("enter the number of rows :"))

for n in range(1, n):

    for column in range(n, 0, -1):

        print(column, end=" ")

    print(" ")