''' Given an integer input N (with k digits), print the sum of the each of the k digits.
only N is given as input k is inferred from the input. For example,if the input is 153, then the output should be 35=(1**2+5**2+3**2)'''
n=int(input())
summ=0
while n>0:
    summ=summ+(n%10)*(n%10)
    n=n//10
print(summ)