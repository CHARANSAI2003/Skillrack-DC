The program must accept N integers as the input. The program must print integers up to the minimum integer among the N integers in the same order as in the input. 
If the minimum integer has occurred more than once then consider the first occurred one. 

Boundary Condition(s): 
1 <= N <= 100
-9999 <= Each integer value <= 9999

Input Format: 
The first line contains the value of N.
The second line contains N integers separated by space(s).

Output Format:
The first line contains integer values separated by a space.

Example Input/Output 1:
Input:
6
-32 99 -88 -95 33 19

Output:
-32 99 -88 -95

Explanation:
The minimum integer value is -95 (among the given 6 integers).
So the integers up to the first occurrence -95 are printed.

Example Input/Output 2:
Input:
9
-89 42 -19 74 -17 85 33 -5 45 

Output:
-89

----------------------------------------------------------------------------------------------------------------

Program:

n=int(input())
m=list(map(int,input().split()))
m1=m.index(min(m))
print(*m[:m1+1])


