The program must accept an integer matrix of size NxN and an integer K as the input. The program must replace all the integers in the matrix which are present below 
the second occurrence of the integer K in each column by '*' and print the matrix as the output.

Boundary Condition(s):
1 <= N <= 100 
1 <= K, Each integer value <= 10^9

Input Format:
The first line contains N and K separated by a space.
The next N lines contain N integers each separated by a space.

Output Format:
The first N lines contain N integers each separated by a space.

Example Input/Output 1:
Input:
4 25
11 25 21 25
14 25 17 26 
25 36 15 25
25 10 18 15

Output:
11 25 21 25
14 25 17 26
25 * 15 25
25 * 18 *

Explanation:
There are three columns (1, 2 and 4) having at least 2 occurrences of 25 in the matrix. 
There are only two columns (2 and 4) which have elements after the second occurrence of 25.
The elements after the second occurrence of 25 in the columns 2 and 4 are replaced by *. 

Example Input/Output 2:
Input:
6 13
13 27 13 13 10 44
31 13 45 22 40 13
42 13 48 13 13 28
13 43 17 19 45 41
30 16 19 30 13 45
16 42 31 18 40 13

Output:
13 27 13 13 10 44
31 13 45 22 40 13
42 13 48 13 13 28
13 * 17 * 45 41
* * 19 * 13 45
* * 31 * * 13

--------------------------------------------------------------------------------------------------

Program:

n,m=list(map(int,input().split()))
a,a1=[],[]
for i in range(n):
    a.append(list(map(int,input().split())))
for i in range(n):
    c=[]
    for j in range(n):
        c.append(a[j][i])
    d=0
    b=[]
    for j in c:
        if d>=2:
            b.append("*")
        elif j==m:
            d+=1
            b.append(j)
        else:
            b.append(j)
    a1.append(b)
for i in range(n):
    c=[]
    for j in range(n):
        c.append(a1[j][i])
    print(*c)    
