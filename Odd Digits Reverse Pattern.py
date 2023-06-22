The program must accept an integer N as the input. The program must print the odd digits from the last digit and remove the last digit of N then again print the odd 
digits from the last digit and remove the last digit and so on. If there is no odd digit in the original N then print -1 as the output.

Boundary Condition(s): 
1 <= N <= 10^7

Input Format:
The first line contains N. 

Output Format:
The first line contains either odd digits as per the condition separated by a space or -1. 

Example Input/Output 1:
Input:
12345

Output:
5 3 1 3 1 3 1 1 1

Explanation:
In 12345, the odd digits 5,3 and 1 are printed.
After removing the last digit the integer becomes 1234.
In 1234, the odd digits 3 and 1 are printed.
After removing the last digit the integer is 123. 
In 123, the odd digits 3 and 1 are printed.
After removing the last digit the integer is 12.
In 12, the odd digit 1 is printed.
After removing the last digit the integer becomes 1. 
In 1, the odd digit 1 is printed.

Example Input/Output 2:
Input: 
2468

Output:
-1

--------------------------------------------------------------------------------------------------------------

Program:

n=input().strip()
a=[]
for i in range(len(n)-1,-1,-1):
    for j in range(i,-1,-1):
        if int(n[j])%2==1:
            a.append(n[j])
if len(a)==0:
    print("-1")
else:
    print(*a)
