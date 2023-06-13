The program must accept an integer matrix of size RxC as the input. The program must reverse each integer in the matrix and then the program must sort the integers in
each column of the matrix in ascending order. Finally, the program must print the modified matrix as the output. 

Boundary Condition(s): 
2 <= R, C <= 100 

Input Format:
The first line contains two integers R and C separated by a space. 
The next R lines contain C integers separated by space(s).

Output Format:
The first R lines contain C integers separated by a space. 

Example Input/Output 1: 
Input:
3 4
19 23 89 22
87 34 45 38
100 23 47 29

Output:
1 32 54 22
78 32 74 83
91 43 98 92

Explanation:
After reversing each integer, the matrix becomes 
91 32 98 22
78 43 54 83
1 32 74 92
After sorting each column, the matrx becomes
1 32 54 22
78 32 74 83
91 43 98 92

Example Input/Output 2:
Input:
5 3 
26 75 23 
14 90 25
92 48 95
80 62 91
54 39 24

Output:
8 9 19
29 26 32
41 57 42
45 84 52
62 93 59

-------------------------------------------------------------------------------------------------------------------

Program:

n,m=list(map(int,input().split()))
b=[]
b1=[]
for i in range(n):
    c=list(map(str,input().split()))
    a=[]
    for j in c:
        a.append(int(j[::-1]))
    b.append(a)
for i in range(m):
    a=[]
    for j in range(n):
        a.append(b[j][i])
    a.sort()
    b1.append(a)
for i in range(n):
    a=[]
    for j in range(m):
        a.append(b1[j][i])
    print(*a)    
