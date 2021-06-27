'''                      CODECHEF   TIC TAC TOE


Tic-tac-toe is a game played between two players on a 3×3 grid. In a turn, a player chooses an empty cell and places their symbol on the cell.
 The players take alternating turns, where the player with the first turn uses the symbol X and the other player uses the symbol O. 
 The game continues until there is a row, column, or diagonal containing three of the same symbol (X or O), 
 and the player with that token is declared the winner. Otherwise if every cell of the grid contains a symbol and nobody won,
  then the game ends and it is considered a draw.

You are given a tic-tac-toe board A after a certain number of moves, consisting of symbols O, X, and underscore(_). 
Underscore signifies an empty cell.

Print

1: if the position is reachable, and the game has drawn or one of the players won.
2: if the position is reachable, and the game will continue for at least one more move.
3: if the position is not reachable.
Note:

Starting from an empty board, reachable position means that the grid is possible after a finite number of moves in the game 
where the players may or may not be playing optimally.
The answer for each testcase should be with respect to the present position and independent of the results in the further successive moves.
Input
The first line contains an integer T, the number of test cases. Then the test cases follow.
Each test case contains 3 lines of input where each line contains a string describing the state of the game in ith row.
Output
For each test case, output in a single line 1, 2 or 3 as described in the problem.

Constraints
1≤T≤39
Aij∈{X,O,_}
Subtasks
Subtask #1 (100 points): Original Constraints

Sample Input
3
XOX
XXO
O_O
XXX
OOO
___
XOX
OX_
XO_
Sample Output
2
3
1
Explanation
Test Case 1: The board is reachable, and although no player can win from this position, still the game continues.

Test Case 2: There can't be multiple winners in the game.

Test Case 3: The first player is clearly a winner with one of the diagonals.'''

#__________________________________________________________________________________
# cook your dish here
def eq(x,y,z):
    if(x==y and y==z):
        return 1 
    else :
        return 0 
def wincomb(a):
    xwin, zwin =0, 0
    for i in range(0,3):
        if a[0][i]!="_" and a[1][i]!="_" and a[2][i]!="_" and eq(a[0][i], a[1][i],a[2][i]):
            if a[0][i]=="X":
                xwin+=1
            else :
                zwin+=1 
        if a[i][0]!="_" and a[i][1]!="_" and a[i][2]!="_" and eq(a[i][0], a[i][1],a[i][2]):
            if a[i][0]=="X":
                xwin+=1 
            else:
                zwin+=1 
    if a[0][0]!="_" and a[1][1]!="_" and a[2][2]!="_" and eq(a[0][0], a[1][1],a[2][2]):
        if a[1][1]=="X":
            xwin+=1 
        else:
            zwin+=1 
    if a[0][2]!="_" and a[1][1]!="_" and a[2][0]!="_" and eq(a[0][2], a[1][1],a[2][0]):
        if a[1][1]=="X":
            xwin+=1 
        else:
            zwin+=1
    return [xwin, zwin]
T=int(input())
for i in range(0,T):
    mat=[]
    u, x, z = 0, 0, 0
    for k in range(0,3):
        a=input()
        u=u+a.count("_")
        x=x+a.count("X")
        mat.append(a)
    z=9-x-u
    if x<z or x-z>1 :
        print(3)
        continue
    wc=wincomb(mat)
    if wc[0] and wc[1]:
        print(3)
    elif wc[0]==1 and u%2==1 :
        print(3)
    elif wc[1]==1 and u%2==0 :
        print(3)
    elif wc[0] or wc[1] :
        print(1)
    elif u==0:
        print(1)
    else:
        print(2)