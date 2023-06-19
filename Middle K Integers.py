The program must accept N integers and an integer K as the input. The program must print middle K integers in the reverse order in the N integers as the output.
Note: Both the integers N and K are odd or both the integers are even.

Boundary Condition(s): 
1 <= N <= 10^5
1 <= K <= N

Input Format:
The first line contains the two integers N and K separated by a space.
The second line contains N integers separated by space(s). 

Output Format:
The first line contains middle K integers in the reverse order. 

Example Input/Output 1:
Input:
13 5
20 10 30 40 5 15 50 25 35 130 110 120 45

Output:
35 25 50 15 5

Explanation: 
The middle 5 integers are 5, 15, 50, 25 and 35.
In the reverse order, the values are 35, 25, 50, 15, 5. 
Hence the output is 35 25 50 15 5

Example Input/Output 2:
Input:
10 4
89 12 15 50 65 13 52 28 15 80

Output:
52 13 65 50

------------------------------------------------------------------------------------------------------------------------------

Program:

n,m=list(map(int,input().split()))
a=list(map(int,input().split()))
c=0
if m%2==0:
    c=(n//2)+((m//2)-1)
else:
    c=(n//2)+(m//2)
for i in range(m):
    print(a[c],end=" ")
    c-=1

