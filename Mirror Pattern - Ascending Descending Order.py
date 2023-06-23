Accept an integer N as the input. The program must print the mirror pattern as shown in the Example Input/Output section below.

Boundary Condition(s):
2 <= N <= 50 

Input Format:
The first line contains the value of N. 

Output Format: 
The first N*N lines contain the mirror pattern.

Example Input/Output 1:
Input:
3

Output:
1
23 
456
654 
32
1

Example Input/Output 2:
Input:
5

Output:
1
23
456
78910
1112131415 
1514131211
10987
654
32
1

-----------------------------------------------------------------------------------------

Program:

n=int(input())
a=1
c=[]
for i in range(n):
    b=[]
    for j in range(0,i+1):
        b.append(a)
        a+=1
    print(*b,sep="") 
    c.append(b[::-1])
c=c[::-1]    
for i in c:
    print(*i,sep="")
