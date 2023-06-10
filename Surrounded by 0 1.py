The program must accept an integer matrix of size NxN containing only 0's and 1's as the input. The program must print the count of 0's which are surrounded by 1's on
all four sides and the count of 1's which are surrounded by 0's on all four sides as the output. 

Boundary Condition(s):
1 <= N <= 100

Input Format:
The first line contains N.
The next N lines contain N integers each separated by a space.

Output Format:
The first line contains two integers separated by a space as the per the given condition.

Example Input/Output 1:
Input: 
5
0 1 0 1 0
1 0 1 0 1
0 1 0 1 0
0 0 1 0 0
0 0 0 0 0

Output: 
3 4 

Explanation: 
The 0's which are surrounded by four 1's are at the following postions (2,2), (2,4) and (3,3).
The 1's which are surrounded by four 0's are at the following positions (2,3), (3,2), (3,4) and (4,3).

Example Input/Output 2:
Input:
6
0 0 1 1 1 0
0 1 0 1 0 1
1 0 1 1 0 1
0 1 1 0 0 0
1 1 1 0 1 0
0 1 0 0 0 0

Output: 
2 2

-------------------------------------------------------------------------------------------------------------

Program:

n=int(input())
a=[]
z=0
o=0
for i in range(n):
    a.append(list(map(int,input().split())))
for i in range(1,len(a)-1):
    c=a[i]
    for j in range(1,len(a)-1):
        if c[j]==0:
            if c[j-1]==1 and c[j+1]==1 and a[i-1][j]==1 and a[i+1][j]==1:
                z+=1
        elif c[j]==1:
            if c[j-1]==0 and c[j+1]==0 and a[i-1][j]==0 and a[i+1][j]==0:
                o+=1
print(z,o)                

