The program must accept a string S and integer X as the input. For every X characters in S, the program must swap the first and last character in the X characters. 
Finally, the program must print the modified string as the output. 
Note: The length of S is always divisible by X.

Boundary Condition(s):
2 <= Length of S <= 10000
2 <= X <= Length of S 

Input Format:
The first line contains the string S and the integer X separated by a space.

Output Format:
The first line contains the modified string.

Example Input/Output 1:
Input:
tacgod 3

Output:
catdog

Explanation: 
The first 3 characters are 't', 'a' and 'c'.
After swapping the first and last character, the string becomes "catgod".
The second 3 characters are 'g', 'o' and 'd'. 
After swapping the first and last character, the string becomes "catdog".
Hence the output is catdog

Example Input/Output 2: 
Input:
oDnwolda 2

Output:
Download

---------------------------------------------------------------------------------------------------

Program:

n,m=list(map(str,input().split()))
n=list(n)
m=int(m)
a=0
for i in range(0,len(n),m):
    c1,c2=n[a],n[a+m-1]
    n[a]=c2
    n[a+m-1]=c1
    a+=m
print(*n,sep="")   
