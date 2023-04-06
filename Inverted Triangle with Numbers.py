The program must accept an integer N as the input. The program must print the desired pattern as shown in the Example Input/Output section.

Boundary Condition(s):
1 <= N <= 50

Input Format:
The first line contains the value of N.

Output Format:
The first N lines containing the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
Input: 
3

Output:
1 * 2 * 3
- 5 * 4
- - 6

Example Input/Output 2:
Input: 
4

Output:
1 * 2 * 3 * 4
- 7 * 6 * 5
- - 8 * 9
- - - 10

---------------------------------------------------------------------------------------

Program: 

  
n=int(input())
m=1
a=[]
n1=n
n2=0
for i in range(n):
    for j in range(i+1):
        a.append(m)
        m+=1
for i in range(n):
    c=a[n2:n1]
    c1=len(c)
    if i%2==0:
        a1=[]
        for j in range(len(c)):
            if j==0:
                c2=i*"- "
                a1.append(c2+str(c[j]))
            else:
                c2=a1.append("* "+str(c[j]))
                
        print(*a1)
    else:
        c=c[::-1]
        a1=[]
        for j in range(len(c)):
            if j==0:
                c2=i*"- "
                a1.append(c2+str(c[j]))
            else:
                c2=a1.append("* "+str(c[j]))
        print(*a1)        
    n2+=c1
    n1+=c1-1 
