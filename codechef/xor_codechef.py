 ''' XOR CODECHEF

For a given N, find the number of ways to choose an integer x from the range [0,2N−1] such that x⊕(x+1)=(x+2)⊕(x+3), where ⊕ denotes the bitwise XOR operator.

Since the number of valid x can be large, output it modulo 109+7.

Input
The first line contains an integer T, the number of test cases. Then the test cases follow.
The only line of each test case contains a single integer N.
Output
For each test case, output in a single line the answer to the problem modulo 109+7.

Constraints
1≤T≤105
1≤N≤105
Subtasks
Subtask #1 (100 points): Original Constraints

Sample Input
2
1
2
Sample Output
1
2
Explanation
Test Case 1: The possible values of x are {0}.

Test Case 2: The possible values of x are {0,2}.'''

# cook your dish here
def myfunction(new1 ,new2 ,new3):
    myresult=1 
    new1=new1%new3
    if new1==0:
        return 0
    while(new2> 0):
        if(new2 & 1):
            myresult=(myresult*new1) %new3
        new2=new2>>1 
        new1=(new1*new1)%new3
    return (myresult)
mymod=1000000007
t=int(input())
for i in range(t):
    n=int(input())
    myans=myfunction(2,n-1,mymod)
    print(myans)