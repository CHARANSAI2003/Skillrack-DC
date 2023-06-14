The program must accept a string value S as the input. The program must print the characters which are present at the odd positions if the count of vowels in S is odd. 
Else the program must print the characters which are present at the even positions as the output. If there is no vowel in the string S then the program must print -1 as
the output.

Boundary Condition(s): 
2 <= Length of S <= 100

Input Format: 
The first line contains the string S.

Output Format:
The first line contains either the characters which are present at the odd or even positions or -1.

Example Input/Output 1:
Input:
apple

Output: 
pl

Explanation:
In the word apple, there are two vowels. Here the count 2 is even.
Hence the characters at the even positions are printed.
Hence the output is pl 

Example Input/Output 2:
Input:
rhythm

Output: 
-1

-----------------------------------------------------------------------------------------------------------

Program:

n=input().strip()
a="aeiou"
c=0
for i in n:
    if i in a:
        c+=1
if c==0:
    print("-1")
else:
    if c%2==0:
        for i in range(1,len(n),2):
            print(n[i],end="")
    else:
        for i in range(0,len(n),2):
            print(n[i],end="")
