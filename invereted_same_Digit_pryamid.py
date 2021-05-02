n=int(input("Enter the number of rows : "))

num = int(input(" enter the number : "))

for i in range(n, 0, -1):

    for j in range(0, i):

        print(num, end=" ")

    print("\r")