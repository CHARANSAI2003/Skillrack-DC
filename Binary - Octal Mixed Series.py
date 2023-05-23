The program must accept two integers X and N as the input. The program must form a series of N integers based on the following conditions. 
- The first term of the series must be the binary representation of X. 
- The second term of the series must be the octal representation of X+1. 
- The third term of the series must be the binary representation of X+2. 
- The fourth term of the series must be the octal representation of X+3 and so on. 
Finally, the program must print the series of N integers as the output.

Boundary Condition(s):
1 <= X, N <= 10^5

Input Format:
The first line contains the values of X and N separated by a space. 

Output Format: 
The first line contains the first N terms of the series separated by a space as per the given conditions.

Example Input/Output 1: 
Input:
5 6

Output:
101 6 111 10 1001 12

Explanation:
The 1st term of the series is the binary representation of 5 (101)2.
The 2nd term of the series is the octal representation of 6 (6)8. 
The 3rd term of the series is the binary representation of 7 (111)2.
The 4th term of the series is the octal representation of 8 (10)8.
The 5th term of the series is the binary representation of 9 (1001)2. 
The 6th term of the series is the octal representation of 10 (12)8. 

Example Input/Output 2:
Input:
150 5

Output:
10010110 227 10011000 231 10011010

----------------------------------------------------------------------------------------------------------

Program:

n,m=list(map(int,input().split()))
for i in range(m):
    if i%2==0:
        print(bin(n)[2:],end=" ")
    else:
        print(oct(n)[2:],end=" ")
    n+=1    
