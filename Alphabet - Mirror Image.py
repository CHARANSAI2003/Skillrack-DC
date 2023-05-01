The program must accept an integer N as the input. The program must print the desired pattern as shown in the Example Input/Output section. 

Boundary Condition(s): 
1 <= N <= 26 

Input Format:
The first line contains N.

Output Format:
The first N lines contain the pattern as shown in the Example Input/Output section.

Example Input/Output 1:
Input:
3

Output: 
a b c * c b a
a b * * * b a
a * * * * * a

Example Input/Output 2:
Input:
4

Output:
a b c d * d c b a
a b c * * * c b a
a b * * * * * b a 
a * * * * * * * a

---------------------------------------------------------------------------------------------------------

Program:

n=int(input())
m="abcdefghijklmnopqrstuvwxyz"
a=[]
for i in range(n):
    c=m[:(i+1)]
    c1=[]
    for j in c:
        c2=j+""
        c1.append(c2)
    a.append(c1)
a1=a[::-1]
a2=[]
z=1
for i in range(1,n+1):
    c=z*"*"
    a2.append(c)
    z+=2
for i in range(n):
    c=a1[i][::-1]
    k=[]
    for j in a1[i]:
        k.append(j)
    for j in a2[i]:
        k.append(j)
    for j in c:
        k.append(j)
    print(*k)
    
