The program must accept an integer N as the input. The program must print the integers from 1 to N having all their digits as odd.

Boundary Condition(s):
1 <= N <= 10^8

Input Format:
The first line contains the value of N.

Output Format: 
The first line contains the integers separated by a space as per the given conditions.

Example Input/Output 1:
Input:
12

Output: 
1 3 5 7 9 11

Explanation: 
2, 4, 6, 8, 10 and 12 are having even digits in it.
So they are not printed. 
The integers from 1 to 12 having all their digits as odd are printed (1 3 5 7 9 11).

Example Input/Output 2:
Input:
55

Output:
1 3 5 7 9 11 13 15 17 19 31 33 35 37 39 51 53 55

--------------------------------------------------------------------------------------------------------------------------

Program:

n=int(input())
for i in range(1,n+1):
    c=str(i)
    s=""
    for j in c:
        if int(j)%2!=0:
            s+=j 
    if len(c)==len(s):
        print(s,end=" ")        

