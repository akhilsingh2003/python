number=int(input("Enter the number "))
count=0
for i in range(2,number):
    if number%i==0 :        
        print(number," is not prime number")
        break
else:
    print("yes,it is a prime number")        
