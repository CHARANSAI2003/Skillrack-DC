The program must accept a character matrix of size RxC as the input. The program must print YES if all the vowels (only lowercase vowels) occur at least once in every row 
and every column. Else the program must print NO as the output. 

Boundary Condition(s):
1 <= R, C <= 50

Input Format: 
The first line contains the values of R and C separated by a space.
The next R lines contain C alphabets each separated by a space.

Output Format:
The first line contains either YES or NO.

Example Input/Output 1:
Input: 
5 6
a e i a o u
e i o e u a
i o u i a e
o u a o e i
u a e u i o

Output:
YES

Explanation:
All the vowels occur at least once in every row and every column. So YES is printed.

Example Input/Output 2:
Input:
7 6
e j e u u i
a y m n o f 
a n h i c q
e i p u o o
e o a e t q
e e o o a e
u n u n k e

Output: 
NO

-----------------------------------------------------------------------------------------------------------------

Program:

n,m=list(map(int,input().split()))
k,k2=0,0
a1=[]
for i in range(n):
    c=list(map(str,input().split()))
    a1.append(c)
    z1=c.count("a")
    z2=c.count("e")
    z3=c.count("i")
    z4=c.count("o")
    z5=c.count("u")
    if z1>0 and z2>0 and z3>0 and z4>0 and z5>0:
        k+=1
for i in range(m):
    a=[]
    for j in range(n):
        c=a1[j][i]
        a.append(c)
    z1=a.count("a")
    z2=a.count("e")
    z3=a.count("i")
    z4=a.count("o")
    z5=a.count("u")
    if z1>0 and z2>0 and z3>0 and z4>0 and z5>0:
        k2+=1 
if k==n and k2==m:
    print("YES")
else:
    print("NO")

