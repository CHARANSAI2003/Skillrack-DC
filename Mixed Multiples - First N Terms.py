The program must accept three integers X, Y and N as the input. The program must form a series of integers where the odd terms are multiples of X in ascending order 
and the even terms are multiples of Y in ascending order. Then the program must print the first N terms of the series as the output. 

Boundary Condition(s):
1 <= X, Y <= 10^5
1 <= N <= 10^8

Input Format:
The first line contains the values of X, Y and N separated by a space.

Output Format: 
The first line contains the first N terms of the series separated by a space as per the given conditions. 

Example Input/Output 1:
Input:
2 5 10

Output:
2 5 4 10 6 15 8 20 10 25 

Explanation: 
The odd terms in the series are 2, 4, 6, 8, 10 and so on.
The even terms in the series are 5, 10, 15, 20, 25 and so on.
Here the first 10 terms in the mixed series are 2 5 4 10 6 15 8 20 10 25. 
So they are printed as the output. 

Example Input/Output 2: 
Input:
11 6 7 

Output:
11 6 22 12 33 18 44

-------------------------------------------------------------------------------------------------------------------------------

Program:

a,b,c=list(map(int,input().split()))
if c%2==0:
    x,y=[],[]
    for i in range(1,c//2+1):
        x.append(i*a)
        y.append(i*b)
    z=[]    
    for i in range(c//2):
        z.append(x[i])
        z.append(y[i])
    print(*z)    
else:
    x,y=[],[]
    for i in range(1,c//2+2):
        x.append(i*a)
    for i in range(1,c//2+1):
        y.append(i*b)
    z=[]
    for i in range(c//2):
        z.append(x[i])
        z.append(y[i])
    z.append(x[-1])
    print(*z)
        
