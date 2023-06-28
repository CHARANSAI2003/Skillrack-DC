The program must accept an integer matrix of size RxC as the input. The program must print the column number which has the most number of negative numbers in the given
matrix as the output. If more than one column have the most number of negative numbers then the program must print the first ocurring such column number as the output.
If the matrix does not contain any negative element then the program must print -1 as the output. 

Boundary Condition(s):
1 <= R, C <= 100 

Input Format:
The first line contains two integers R and C separated by a space.
The next R lines contain C integers separated by space(s).

Output Format:
The first line contains either the column number which has the most number of negative numbers or -1.

Example Input/Output 1:
Input: 
3 4
10 20 11 -12 
-22 -23 89 -79
-89 10 29 -12

Output:
4

Explanation:
The 1st column contains 2 negative numbers.
The 2nd column contains 1 negative number.
The 3rd column does not contain any negative number. 
The 4th column contains 3 negative numbers.
Here, the column 4 has the most number of negative numbers.
Hence the output is 4.

Example Input/Output 2:
Input:
3 3
11 91 81
90 10 20
89 88 87 

Output:
-1

------------------------------------------------------------------------------------------------------------------

Program:

n,m=list(map(int,input().split()))
a=[]
d=[]
for i in range(n):
    c=list(map(int,input().split()))
    a.append(c)
for i in range(m):
    c=[]
    for j in range(n):
        c.append(a[j][i])
    b=0    
    for j in c:
        if j<0:
            b+=1
    d.append(b) 
if max(d)>0:
    print(d.index(max(d))+1)    
else:
    print("-1")
