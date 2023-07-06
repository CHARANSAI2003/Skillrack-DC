The program must accept a string S and an integer X as the input. The program must print the first X consonants in the string S as the output. If the number of consonants
in the string S is less than X then the program must print -1 as the output. 
Note: The string S contains only alphabets. 

Boundary Condition(s):
1 <= Length of S <= 100 
1 <= X <= Length of S

Input Format:
The first line contains the string S. 
The second line contains the value of X. 

Output Format:
The first line contains either the first X consonants in S or -1.

Example Input/Output 1: 
Input:
SkillRack
5

Output:
SkllR 

Explanation:
The first 5 consonants in the string "SkillRack" are S, k, l, l and R.
So they are printed as the output.

Example Input/Output 2:
Input:
Dengue 
6

Output:
-1

----------------------------------------------------------------------------------------------------------------

Program:

n=input().strip()
m=int(input())
a=[]
for i in n:
    if i not in "aeiouAEIOU":
        a.append(i)
if len(a)>=m:
    print(*a[:m],sep="")
else:
    print("-1")
