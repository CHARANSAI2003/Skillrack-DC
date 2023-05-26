The program must accept two lines of string values with space S1 and S2 as the input. The program must remove all the words in S2 from S1 and print the remaining word
s as the output. If all the words in S1 are present in S2 then the program must print -1 as the output.
Note: There is exactly one space between every two words.

Boundary Condition(s):
1 <= Length of S1 and S2 <= 1000

Input Format:
The first line contains S1.
The second line contains S2.

Output Format: 
The first line contains the words in S1 as per the given condition or -1. 

Example Input/Output 1:
Input:
join us for the party
party with us in home

Output: 
join for the 

Explanation:
The words in S2 appearing in S1 are "us" and "party".
They are removed. Hence the output is join for the

Example Input/Output 2:
Input:
cycling is good 
I like cycling and it is good 

Output:
-1

---------------------------------------------------------------------------------------------------------------

Program:

n=list(map(str,input().split()))
m=list(map(str,input().split()))
a=[]
for i in n:
    c=m.count(i)
    if c==0:
        a.append(i)
if len(a)==0:
    print("-1")
else:
    print(*a)
