The program must accept an integer matrix of size RxC and an integer X as the input. The program must reverse last X integers in each row. Finally, the program must 
print the modified matrix as the output.

Boundary condition(s): 
1 <= R, C <= 100
1 <= X <= C

Input Format:
The first line contains two integers R and C separated by a space.
The next R lines contain C integers separated by space(s).
The last line contains the integer X.

Output Format:
The first R lines contain C integers separated by space(s).

Example Input/Output 1:
Input:
3 5
44 12 12 47 37
18 18 11 11 19
38 27 23 40 14
3

Output: 
44 12 37 47 12
18 18 19 11 11
38 27 14 40 23

Explanation: 
The Last three integers in the 1st row are 12, 47 and 37. 
Reverse those integers and then print them as the output. 
44 12 37 47 12 The Last three integers in the 2nd row are 11, 11 and 19. 
Reverse those integers and then print them as the output. 
44 12 37 47 12
18 18 19 11 11
The Last three integers in the 3rd row are 23, 40 and 14. 
Reverse those integers and then print them as the output. 
44 12 37 47 12 
18 18 19 11 11
38 27 14 40 23

Example Input/Output 2: 
Input: 
3 3
1 2 3
4 5 6
7 8 9
2 

Output:
1 3 2 
4 6 5
7 9 8

----------------------------------------------------------------------------------------------------------

Program:

n,m=list(map(int,input().split()))
a=[]
for i in range(n):
    c=list(map(int,input().split()))
    a.append(c)
x=int(input())
for i in range(n):
    c=a[i]
    y=c[-x:]
    y=y[::-1]
    y1=c[:-x]
    k=y1+y 
    print(*k)
