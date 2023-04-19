The program must accept an integer N as the input. The program must remove all the occurrences of the unit digit of N in the integer N. Then the program must print the 
modified value of N as the output. If all the digits in N are removed then the program must print -1 as the output.

Boundary Condition(s):
1 <= N <= 10^9 

Input Format:
The first line contains the value of N.

Output Format:
The first line contains the modified value of N or -1.

Example Input/Output 1:
Input:
480454

Output: 
805

Explanation:
The unit digit of N is 4. So all the occurrences of 4 are removed in the integer 480454. Hence the output is 805

Example Input/Output 2:
Input:
1005201

Output: 
520

Example Input/Output 3:
Input:
6666

Output:
-1

---------------------------------------------------------------------------------------

Program:

n=input().strip()
n1=n[-1]
a=""
for i in n:
    if i!=n1:
        a+=i 
if len(a)==0:
    print("-1")
else:
    print(int(a))
          
