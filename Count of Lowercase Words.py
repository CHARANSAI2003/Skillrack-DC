The program must accept a string S as the input. The program must print the count of words having only lowercase alphabets as the output.

Boundary Condition(s):
1 <= Length of S <= 100

Input Format:
The first line contains the string S.

Output Format:
The first line contains the count of words having only lowercase alphabets.

Example Input/Output 1:
Input:
Learning never exhausts the mind

Output: 
4

Explanation: 
There are 4 words having only lowercase alphabets. 
They are "never", "exhausts", "the" and "mind".

Example Input/Output 2:
Input: 
Asdf ;lkj AWERQFA ;OIUPJ; gFtFrF hJyJuJ 

Output: 
0

----------------------------------------------------------------------------------

Program:

n=input().split()
count=0
for i in range(len(n)):
    c=n[i]
    c1=[]
    for j in c:
        if j.islower():
            c1.append(j)
    if len(c)==len(c1):
        count+=1
print(count)


