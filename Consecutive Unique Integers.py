The program must accept N integers and an integer X as the input. The program must print the count of consecutive X integers (among N integers) in which all the X
integers are different as the output.

Boundary Condition(s):
2 <= N <= 10^4
1 <= X <= N

Input Format:
The first line contains two integers N and X separated by a space. 
The second line contains N integers separated by space(s).

Output Format:
The first line contains count the number of consecutive X integers in which all the X integers are unique.

Example Input/Output 1:
Input: 
6 3
1 2 3 4 4 5

Output:
2

Explanation:
X = 3, The first three integers are 1, 2 and 3.
Here all the integers are unique.
So the count is 1.
The next three consecutive integers are 2, 3 and 4.
Here all the integers are unique.
So the count becomes 2.
The next three consecutive integers are 3, 4 and 4.
Here duplicate integers have occurred.
The next three consecutive integers are 4, 4 and 5.
Here duplicate integers have occurred. 
Hence the output is 2

Example Input/Output 2:
Input:
8 5
9 8 1 8 1 2 4 5

Output:
1

------------------------------------------------------------------------------------------------------------------

Program:

n,m=list(map(int,input().split()))
a=list(map(int,input().split()))
count=0
for i in range(n-m+1):
    c=a[i:m]
    m+=1
    k=set(c)
    if len(c)==len(k):
        count+=1
print(count)        

