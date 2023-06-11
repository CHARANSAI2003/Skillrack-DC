The program must accept an integer N as the input. The program must print YES if the binary representation of N is a palindrome. Else the program must print NO as the 
output.

Boundary Condition(s): 
1 <= N <= 10^9 

Input Format: 
The first line contains the value of N.

Output Format:
The first line contains either YES or NO. 

Example Input/Output 1:
Input:
5

Output:
YES

Explanation:
The binary representation of 5 is 101.
Here 101 is a palindrome.
Hence the output is YES

Example Input/Output 2:
Input:
10

Output:
NO

------------------------------------------------------------------------------------------------------------

Program:

n=int(input())
m=bin(n)[2:]
m1=m[::-1]
if m1==m:
    print("YES")
else:
    print("NO")
