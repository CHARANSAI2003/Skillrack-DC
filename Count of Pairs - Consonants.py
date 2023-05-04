The program must accept a string S as the input. The program must print the count of consecutive pairs having the consonants in S as the output. 

Boundary Condition(s):
2 <= length of S <= 1000

Input Format: 
The first line contains the string S.

Output Format:
The first line contains the count of consecutive pairs having consonants in S. 

Example Input/Output 1:
Input:
Apple

Output: 
2

Explanation:
The first consecutive pair of consonants is pp.
The second consecutive pair of consonants is pl.
So 2 is printed as the output. 

Example Input/Output 2:
Input:
ORANGE

Output: 
1

-----------------------------------------------------------------------------------------

Program:

n=input().strip().lower()
a="aeiou"
b=0
for i in range(len(n)-1):
    if n[i] not in a and n[i+1] not in a:
        b+=1
print(b)        


