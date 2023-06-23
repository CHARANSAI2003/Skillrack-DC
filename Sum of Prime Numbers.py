Given an integer matrix of size M*N as input, the program must print the sum of prime numbers present in the given matrix.

Boundary Condition(s):
1 <= M, 
N <= 50

Input Format:
The first line contains the values of M and N separated by a space.
The next M lines contain N elements each separated by space(s).

Output Format:
The first line contains the sum of prime numbers present in the matrix.

Example Input/Output 1:
Input:
3 4
1 2 3 4
5 6 7 8 
9 10 11 12

Output:
28

Explanation :
The prime numbers are 2, 3, 5, 7, 11 and their sum is 28.

Example Input/Output 2:
Input:
3 3
3 4 2
1 2 6
5 4 1

Output:
12 

Explanation :
The prime numbers are 3, 2, 2, 5 and their sum is 12.

----------------------------------------------------------------------------------------------------------------

Program:

n,m=list(map(int,input().split()))
count=0
for i in range(n):
    c=list(map(int,input().split()))
    for j in c:
        a=0
        for k in range(1,j+1):
            if j%k==0:
                a+=1
                
        if a==2:
            count+=j 
print(count)            

