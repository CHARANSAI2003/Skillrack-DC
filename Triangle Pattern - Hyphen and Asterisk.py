The program must accept an integer N as the input. The program must print the desired pattern as shown in the Example Input/Output section.

Boundary Condition(s):
1 <= N <= 100 

Input Format:
The first line contains the value of N. 

Output Format:
The first N lines containing the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
Input:
4

Output:
---**---
--****-- 
-******-
********

Example Input/Output 2:
Input:
7

Output:
------**------
-----****-----
----******----
---********---
--**********-- 
-************- 
**************

-----------------------------------------------------------------------------------------------


Program:

n = int(input())

for i in range(1,n+1):
    leftandright = (n-i)*"-"
    star = (i)*"*"
    print( leftandright + star + star + leftandright)  
  
