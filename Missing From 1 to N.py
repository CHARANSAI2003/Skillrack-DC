The program must accept N integers containing integers from 1 to N with duplicates in any order. The program must print the missing integers from 1 to N among the given
integers in ascending order as the output. 

Boundary Condition(s):
1 <= N <= 10^5

Input Format:
The first line contains N.
The second line contains N integers separated by a space.

Output Format:
The first line contains the missing integers separate by a space.

Example Input/Output 1: 
Input:
5 2 5 5 1 1

Output: 
3 4

Explanation:
The integers 3 and 4 are missing in the 5 integers 2 5 5 1 1.
Hence 3 and 3 are printed as the output.

Example Input/Output 2:
Input: 
7 2 4 4 4 5 6 6

Output:
1 3 7

------------------------------------------------------------------------------------------------

Program:

n=int(input())
m=set(list(map(int,input().split())))
for i in range(1,n+1):
    if i not in m:
        print(i,end=" ")

