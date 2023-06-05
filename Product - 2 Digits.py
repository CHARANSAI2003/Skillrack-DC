The program must accept an integer N as the input. If the number of digits in N is even then the program must print product of every two digits in N as the output. If the
number of the digits in N is odd then the program must print the product of every two digits in N then it must print the remaining digit (last digit) as it is as the 
output.

Boundary Condition(s):
1 <= N <= 10^15

Input Format:
The first line contains the integer N.

Output Format: 
The first line contains the integers separated by space as per the given condition.

Example Input/Output 1:
Input:
1234 

Output:
2 12

Explanation:
The number of digits in 1234 is 4 which is even.
The product of the first two digits is 2 (1 * 2).
The product of the next two digits is 12 (3 * 4).
Hence the output is 2 12

Example Input/Output 2:
Input: 
19849

Output:
9 32 9

----------------------------------------------------------------------------------------------------------------------

Program:

n=input().strip()
c1=0
c2=2
m1=0
c=[]
while len(n)-1>c1:
    m=n[c1:c2]
    c.append(int(m[0])*int(m[1]))
    c1+=2
    c2+=2
    m1+=1
if len(n)%2==1:
    c.append(n[-1])
    print(*c)
else:
    print(*c)

