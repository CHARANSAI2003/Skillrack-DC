The program must accept an integer matrix of size NxN as the input. The program must find the sum S of elements in the main diagonal and the opposite diagonal of the matrix. 
Then the program must replace all the elements in the main diagonal and the opposite diagonal by S. Finally, the program must print the modified matrix as the output.

Boundary Condition(s):
2 <= N <= 50

Input Format:
The first line contains N.
The next N lines contain N integers each separated by space(S). 

Output Format:
The first N lines contain N integers of the modified matrix each separated by space(s). 

Example Input/Output 1:
Input:
4
17 28 47 40
24 43 40 43
50 38 44 33
44 22 46 41

Output:
307 28 47 307
24 307 307 43
50 307 307 33 
307 22 46 307

Explanation:
The elements in the main diagonal are 17 43 44 and 41. 
The elements in the opposite diagonal are 40 40 38 and 44.
The sum of elements in the main diagonal and the opposite diagonal is 307.
So all the elements in the main diagonal and the opposite diagonal are replaced by 307. 
Hence the output is 
307 28 47 307 
24 307 307 43
50 307 307 33 
307 22 46 307

Example Input/Output 2: 
Input:
3
49 32 22
50 39 23
24 47 40 

Output:
174 32 174
50 174 23 
174 47 174

Explanation: 
The elements in the main diagonal are 49 39 and 40.
The elements in the opposite diagonal are 22 39 and 24.
Here 39 is common for both the diagonals. 
So only one 39 is considered to find the sum S. 
The sum of elements in the main diagonal and the opposite diagonal is 174.
So all the elements in the main diagonal and the opposite diagonal are replaced by 174. 
Hence the output is 
174 32 174
50 174 23
174 47 174

--------------------------------------------------------------------------------------------------------------------------------------------------

Program:

n=int(input())
m=0
a=[]
for i in range(n):
    c=list(map(int,input().split()))
    a.append(c)
    if n%2==0:
        m+=c[i]+c[-(i+1)]
    else:
        if n//2==i:
            if len(c)//2:
                m+=c[i]
        else:
            m+=c[i]+c[-(i+1)]
    
m2=[]    
for i in range(n):
    k=a[i]
    m1=[]
    for j in range(len(k)):
        if i==j:
            m1.append(m)
        else:
            m1.append(a[i][j])
    m1=m1[::-1]
    m2.append(m1)
for i in range(n):
    k1=m2[i]
    m1=[]
    for j in range(len(k1)):
        if i==j:
            m1.append(m)
        else:
            m1.append(m2[i][j])
    m1=m1[::-1]
    print(*m1)
    
