The program must accept a string S as the input. The program must print all the vowels in the second half of the string S in the given order. Then the program must print 
all the vowels in the first half of the string S in the given order as the output. If there is no vowel in S then the program must print -1 as the output.

Note: The length of S is always even. 

Boundary Condition(s): 
2 <= Length of S <= 100

Input Format:
The first line contains the string S.

Output Format:
The first line contains either the vowels based on the above conditions or -1.

Example Input/Output 1:
Input:
farmer 

Output: 
ea

Explanation: 
The second half of the string "farmer" has only one vowel e. So it is printed.
The first half of the string "farmer" has only one vowel a. 
So it is printed. Hence the output is ea

Example Input/Output 2:
Input:
CONVERSATION

Output: 
AIOOE

Example Input/Output 3:
Input:
yhnygv

Output:
-1

-----------------------------------------------------------------


Program:

n=input().strip()
m1=n[(len(n)//2):]
m2=n[:(len(n)//2)]
a=[]
for i in m1:
    if i in "aeiouAEIOU":
        a.append(i)
for i in m2:
    if i in "aeiouAEIOU":
        a.append(i)
if len(a)==0:
    print("-1")
else:
    print(*a,sep="")
