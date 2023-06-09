The program must accept an NxN matrix as the input. The program must replace the digits in each integer by '*' if the integer is divisible by its unit digit and print it
as the output. Else the program must print the integer without any modification as the output. 

Boundary Conditions(s):
1 <= N <= 100 
1 <= Each integer value <= 10^5

Input Format:
The first line contains N. 
The next N lines contain N integers each separated by a space.

Output Format: 
The first N lines contain the modified matrix.

Example Input/Output 1:
Input:
4
163 122 84 97
155 246 192 124
44 97 57 167
46 36 278 281 

Output:
163 *** ** 97
*** *** *** ***
** 97 57 167
46 ** 278 ***

Explanation:
The integers which are divisible by their unit digits are 122, 84, 155, 246, 192, 124, 44, 36 and 281.
The digits in these integers are replaced as '*' and printed. 

Example Input/Output 2:
Input:
5
973 1416 1387 998 727
877 995 1352 477 1195 
74 965 1345 238 591 
848 182 696 314 7
259 764 187 1002 428 

Output:
973 **** 1387 998 727
877 *** **** 477 ****
74 *** **** 238 ***
*** *** *** 314 *
259 *** 187 **** 428

--------------------------------------------------------------------------------------------------------------------

Program:

a=int(input())
for i in range(a):
    c=list(map(int,input().split()))
    b=[]
    for j in c:
        if int(str(j)[-1])!=0 and int(str(j))%int(str(j)[-1])==0:
            b.append(len(str(j))*"*")
        else:
            b.append(j)
    print(*b)
