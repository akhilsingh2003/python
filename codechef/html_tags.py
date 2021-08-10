'''
In addition to CP, Chef recently developed an interest in Web Development and
 started learning HTML. Now he wants to create his own HTML Code Editor. 
 As a subproblem, he wants to check if a typed HTML closing tag has correct syntax or not.

A closing HTML tag must:

Start with "</"
End with ">"
Have only lower-case alpha-numeric characters as its body (between "</" and ">"). 
That is, each character of the body should either be a digit or a lower-case English letter.
Have a non-empty body.
Help Chef by printing "Success" if the tag is fine. If not, print "Error".

Input
The first line contains an integer T, the number of test cases. Then T test cases follow.
Each test case is a single line of input, a string describing the tag we need to check.
Output
For each test case, output in a single line, "Success" if it is a valid closing tag 
and "Error" otherwise (without quotes).

You may print each character of the string in uppercase or lowercase (for example,
 the strings "SuccEss", "success", "Success", "SUCCESS" et cetera will all be treated as identical).

Constraints
1≤T≤1000
1≤ length(Tag) ≤1000
The characters of the string belong to the ASCII range [33,126] (note that this excludes space.)
Subtasks
Subtask #1 (100 points): Original constraints

Sample Input
5 
</h1>  
Clearly_Invalid  
</singlabharat>  
</5>  
<//aA>  
Sample Output
Success  
Error  
Success
Success
Error
'''
try:

    for i in range(int(input())):
        a=input()
        b=len(a)-1
        if (a[:2]=="</" and a[-1]==">"):
            if (a[2:b].isalnum() and a[2:b].islower()) :
                print("Success")
            elif (a[2:b].isnumeric()):
                print("Success")
            else:
                print("Error")
        else:
            print("Error")
except:
    pass            