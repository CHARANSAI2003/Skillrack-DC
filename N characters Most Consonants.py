The program must accept a string S and an integer N as the input. The program must print the first N characters of S if it contains more consonants than the number of 
consonants in the last N characters of S as the output. Else the program must print the last N characters of S as the output. If both the first N and last N characters
contain the same number of consonants then the program must print the entire string without any modifications as the output. 

Boundary Condition(s):
2 <= Length of string <= 100 
1 <= N <= Length of string 

Input Format: 
The first line contains S and N separated by a space.

Output Format:
The first line contains the string as per the given condition.

Example Input/Output 1:
Input:
tamarind 4 

Output: 
rind

Explanation:
There are 2 consonants in the first 4 characters.
There are 3 consonants in the last 4 characters.
Hence the last 4 characters are printed. 

Example Input/Output 2:
Input:
basic 2 

Output:
basic


-------------------------------------------------------------------------------------------------------------

Program: 

n,m=input().split()
m=int(m)
c1=n[:m]
c2=n[-m:]
count1=0
count2=0
for i in c1:
    if i in "aeiouAEIOU":
        count1+=1
for i in c2:
    if i in "aeiouAEIOU":
        count2+=1
if count1==count2:
    print(n)
elif count1>count2:
    print(c2)
else:
    print(c1)
