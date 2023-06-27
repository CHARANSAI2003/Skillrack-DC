The program must accept a string value S and an integer N as the input. The program must remove the characters which are present at the positions of multiples of N and then
print the modified string as the output.

Boundary Condition(s): 
1 <= Length of S <= 100
2 <= N <= Length of S

Input Format: 
The first line contains the string S and the integer N.

Output Format:
The first line contains the modified string.

Example Input/Output 1:
Input:
SQUIRRELED 3

Output:
SQIRELD

Explanation:
In the string SQUIRRELED, the characters which are present at the positions of multiples of 3 are U, R and E. 
So remove the characters U, R and E in the string SQUIRRELED.
Hence the output is SQIRELD 

Example Input/Output 2: 
Input: 
Banglore 2

Output:
Bnlr

-------------------------------------------------------------------------------------------------------------

Program:

n,m=list(map(str,input().split()))
m=int(m)
for i in range(len(n)):
    if (i+1)%m!=0:
        print(n[i],end="")
