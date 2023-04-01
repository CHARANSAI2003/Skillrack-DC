The program must accept an integer matrix of size RxC as the input. For each integer, the program must print the sum of the elements which are present on its right and below 
the current element as the output. The elements in the last column have no element on their right and the elements in the last row have no elements below them. So consider
the available elements to print the sum. The element which is present in the Rth row and Cth column has no element on its right and below it, so print the same as the output.

Boundary Condition(s):
2 <= R, C <= 100 

Input Format:
The first line contains two integers R and C separated by a space. The next R lines contain C integers separated by space(s).

Output Format:
The first R lines contain C integers separated by space.

Example Input/Output 1:
Input:
3 3
10 20 30
15 25 35
80 70 60 

Output:
35 55 35
105 105 60
70 60 60 

Explanation:
For element 10, the right side and the below elements are 20 and 15 and their sum is 35. So 35 is printed. 
For element 20, the right side and the below elements are 30 and 25 and their sum is 55. So 55 is printed.
For element 30, the element present below is 35. So 35 is printed. For element 15, the right side and the below elements are 25 and 80 and their sum is 105.
So 105 is printed. For element 25, the right side and the below elements are 35 and 70 and their sum is 105. So 105 is printed. For element 35, the below element is 60. 
So 60 is printed. For element 80, the right side element is 70. So 70 is printed. For element 70, the right side element is 60. So 60 is printed. For element 60,
there is no element on its right and down. So 60 is printed.

Example Input/Output 2:
Input:
5 4
10 20 30 40
11 12 13 14
50 60 70 80
21 22 23 24
15 25 35 45

Output:
31 42 53 14
62 73 84 80
81 92 103 24
37 48 59 45
25 35 45 45


----------------------------------------------------------------------------------------------------------------

n,m=list(map(int,input().split()))
a=[]
for i in range(n):
    c=list(map(int,input().split()))
    a.append(c)
for i in range(len(a)):
    if i==len(a)-1:
        c=a[i]
        a1=[]
        for j in range(len(c)):
            if j==len(c)-1:
                c1=c[j]
                a1.append(c1)
            else:
                c1=c[j+1]
                a1.append(c1)
        print(*a1)
    else:
        c=a[i]
        a1=[]
        for j in range(len(c)):
            if j==len(c)-1:
                c1=a[i+1][-1]
                a1.append(c1)
            else:
                c1=a[i+1][j]+c[j+1]
                a1.append(c1)
        print(*a1)

