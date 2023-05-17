The program must accept an integer N as the input. The program must print the desired pattern as shown in the Example Input/Output section. Note: N is always a non-zero 
value. 

Boundary Condition(s):
-100 <= N <= 100

Input Format: 
The first line contains the value of N.

Output Format: 
The first N lines containing the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1: 
Input: 
4

Output: 
1 * * * 
2 3 * *
4 5 6 *
7 8 9 10

Example Input/Output 2:
Input:
-4

Output:
* * * 1
* * 3 2
* 6 5 4
10 9 8 7

-----------------------------------------------------------------------------------------------------

Program:

n=int(input())
m=n
if m>0:
    pass
else:
    m=(-(n))
count = 1   
z=[]
for i in range(1,m+1):
    a=[]
    for j in range(1,m+1):
        if i>=j:
            a.append(count)
            count+=1
        else:
            a.append("*")
    z.append(a)        
if n>0:
    for i in z:
        print(*i)
else:
    for i in z:
        i=i[::-1]
        print(*i)
        
        

