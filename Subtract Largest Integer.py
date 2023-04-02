The program must accept N positive integers as the input. The program must subtract the integers from the largest integer among the N integers and print the modified 
integers as the output.

Boundary Condition(s):
1 <= N <= 1000 

Input Format: 
The first line contains N. The second line contains N integers separated by space.

Output Format:
The first line contains N integers separated by a space.

Example Input/Output 1:
Input:
6 12 40 30 56 21 8

Output:
44 16 26 0 35 48

Explanation:
The largest integer among the N integers is 56.
Each integer is subtracted from 56 and replaced. 

Example Input/Output 2:
Input: 
7 33 23 15 39 30 17 10

Output:
6 16 24 0 9 22 29


----------------------------------------------------------------------------------------------------------------------


Program:


n=int(input())
m=list(map(int,input().split()))
max_m = max(m)
for i in m:
    c=max_m - i
    print(c,end=" ")












