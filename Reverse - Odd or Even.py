The program must accept N integers as the input. The program must print the output based on the following conditions. 
- If the number of even integers is greater than the number of odd integers then the program must print all the even integers in the reverse order followed by
all the odd integers in the given order.
- If the numberof even integers is less than the number of odd integers then the program must print all the odd integers in the reverse order followed by all the
even integers in the given order. 
- If the number of even integers is equal to the number of odd integers then the program must print all the integers in the reverse order.

Boundary Condition(s):
1 <= N <= 100
-10^8 <= Each integer value <= 10^8

Input Format:
The first line contains the value of N.
The second line contains N integers separated by space(s).

Output Format: 
The first line contains either N integers separated by a space or -1 based on the given conditions.

Example Input/Output 1:
Input:
7
21 14 11 13 29 24 15 

Output:
15 29 13 11 21 14 24

Explanation:
The number of odd integers is 5. 
The number of even integers is 2.
Here 5 is greater than 2, so all the odd integers are printed in reverse order followed by all the even integers in the given order.
Hence the output is 15 29 13 11 21 14 24

Example Input/Output 2:
Input: 
4
-12 45 78 -23

Output: 
-23 78 45 -12

----------------------------------------------------------------------------------------------------

Program:

n=int(input())
m=list(map(int,input().split()))
even=[]
odd=[]
for i in m:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
if len(even)>len(odd):
    even=even[::-1]
    k=even+odd
    print(*k)
elif len(even)<len(odd):
    odd=odd[::-1]
    k=odd+even
    print(*k)
else:
    m=m[::-1]
    print(*m)
    

