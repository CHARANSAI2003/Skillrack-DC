The program must accept N integers as the input. The program must print the output based on the following conditions.
- If N is odd then the program must print the middle three integers as the output. 
- If N is even then the program must print the middle four integers as the output. 

Boundary Condition(s): 
5 <= N <= 1000 

Input Format:
The first line contains the integer N.
The second line contains N integers separated by space(s).

Output Format: 
The first line contains either middle three or middle four integers separated by a space based on the conditions mentioned above.

Example Input/Output 1:
Input: 
5 11 22 33 44 55

Output: 
22 33 44

Explanation:
The integer N is odd. So the middle three integers are 22, 33 and 34 (11, 22, 33, 44, 55) are printed.
Hence the output is 22 33 44

Example Input/Output 2:
Input:
8 51 23 43 78 19 25 36 43

Output:
43 78 19 25

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

program:
  
n=int(input())
m=list(map(int,input().split()))
if n%2==0:
    c=n//2 
    k=m[(c-2):c]+m[c:c+2]
    print(*k)
else:
    c=n//2
    k=m[(c-1):c+2]
    print(*k)
    
    
    
