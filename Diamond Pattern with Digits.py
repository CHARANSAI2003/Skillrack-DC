The program must accept an integer N as the input. The program must print the desired pattern as shown in the Example Input/Output section.

Boundary Condition(s):
2 <= N <= 100

Input Format:
The first line contains the integer N.

Output Format:
The lines containing the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
Input:
4

Output: 
---<0>
--<123> 
-<45678>
<9012345>
-<67890>
--<123> 
---<4> 

Example Input/Output 2:
Input:
7

Output:
------<0>
-----<123>
----<45678>
---<9012345>
--<678901234>
-<56789012345>
<6789012345678> 
-<90123456789> 
--<012345678>
---<9012345>
----<67890>
-----<123>
------<4>

-------------------------------------------------------------------------------------------------------------

Program:

n=int(input())
m=0
b=0
c=n
for i in range(0,n):
    a=""
    if i==0:
        if m==9:
            a+=str(m)
            m=0
        else:
            a+=str(m)
            m+=1
    else:
        for j in range(0,b+1):
            if m==9:
                a+=str(m)
                m=0
            else:
                a+=str(m)
                m+=1
    b+=2    
    c-=1
    print(c*"-"+"<"+a+">")   
c1=c  
b=b-4
for i in range(0,n-1):
    a=""
    if i==n-2:
        if m==9:
            a+=str(m)
            m=0
        else:
            a+=str(m)
            m+=1
    else:
        for j in range(0,b+1):
            if m==9:
                a+=str(m)
                m=0
            else:
                a+=str(m)
                m+=1
    b-=2
    c1+=1
    print(c1*"-"+"<"+a+">")

