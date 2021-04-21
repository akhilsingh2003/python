a=input("Enter the string ")
a=a.casefold()
b=a[-1::-1]
if a==b:
    print("yes it is a palindrome")
else:
    print("No it is not a palindrome")    