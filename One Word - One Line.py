The program must accept a space separated string S as the input. The program must print every word in the string in a separate line.

Boundary Condition(s): 
1 <= Length of S <= 100

Input Format: 
The first line contains the string S.

Output Format:
The list of lines containing the word in each line.

Example Input/Output 1:
Input:
hi! how are you?

Output:
hi!
how
are
you?

Example Input/Output 2:
Input:
hello friends 

Output: 
hello 
friends

-------------------------------------------------------------------------------------------------------------

Program:

n=input().split(" ")
for i in n:
    print(i)
