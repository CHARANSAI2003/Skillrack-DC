The program must accept an integer N and a digit D as the input. The program must add the digit D to all the digits of N. Finally, the program must print the modified
value of N as the output. 

Boundary Condition(s): 
1 <= N <= 10^17
0 <= D <= 9 

Input Format:
The first line contains the value of N.
The second line contains the value of D.

Output Format:
The first line contains the modified value of N.

Example Input/Output 1:
Input:
2875 
4

Output:
612119 

Explanation: 
The first digit in 2875 is 2. So the sum of 2 and 4 is 6.
The second digit in 2875 is 8. So the sum of 8 and 4 is 12.
The third digit in 2875 is 7. So the sum of 7 and 4 is 11.
The fourth digit in 2875 is 5. So the sum of 5 and 4 is 9.
Hence the output is 612119 

Example Input/Output 2:
Input: 
90100 
9

Output: 
1891099

-------------------------------------------------------------------------------

Program:

n=input().strip()
m=int(input())
for i in n:
    c=str(int(i)+m)
    print(c,end="")

