The program must accept two integers N1 and N2 as the input. The program must print Valid if the tenth digit or the unit digit of N2 is present in N1. Else the program must
print Invalid as the output.

Boundary Condition(s):
10 <= N1,
N2 <= 99

Input Format:
The first line contains the two integer values N1 and N2 separated by a space.

Output Format:
The first line contains either Valid or Invalid.

Example Input/Output 1: 
Input:
12 23

Output:
Valid

Example Input/Output 2:
Input:
90 13

Output:
Invalid

-----------------------------------------------------------------------------------------------

Program:

n,m=list(map(str,input().split()))
m=m[-2:]
a=[]
for i in m:
    if i in n:
        a.append(i)
if len(a)==0:
    print("Invalid")
else:
    print("Valid")
