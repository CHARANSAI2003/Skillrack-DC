The program must accept an integer N as the input. The program must print YES if all the digits in N are even. Else the program must print the NO as the output.

Boundary Condition(s):
1 <= N <= 10^8

Input Format:
The first line contains the integer N.

Output Format: 
The first line contains either YES or NO. 

Example Input/Output 1:
Input:
2468

Output:
YES

Explanation:
All the digits in 2468 are even.
So YES is printed.

Example Input/Output 2: 
Input: 
277778

Output:
NO

------------------------------------------------------------------------------------------------------------------------------

Program:

n=input().strip()
a=[]
for i in n:
    if int(i)%2==0:
        a.append(1)
if len(a)==len(n):
    print("YES")
else:
    print("NO")
    
    
