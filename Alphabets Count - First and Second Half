The program must accept a string S as the input. The program must find the count of alphabets M which are present between the alphabets a and m (inclusive) in the string S.
Then the program must find the count of alphabets N which are present between the alphabets n and z (inclusive) in the string S. Finally, the program must print the output 
based on the following conditions. -If M is greater than N then print FIRSTHALF. -If N is greater than M then print SECONDHALF. -If M and N are equal then print -1. 
Note: The alphabets in S are only in lower case.

Boundary Condition(s):
1 <= Length of S <= 100

Input Format:
The first line contains the string S.
Output Format:
The first line contains FIRSTHALF or SECONDHALF or -1.

Example Input/Output 1:
Input:
abcdxyz

Output:
FIRSTHALF 

Explanation:
The alphabets a, b, c and d are present between the alphabets a and m.So their count M is 4. 
The alphabets x, y and z are present between the alphabets n and z. So their count N is 3.
Here M is greater than N. So FIRSTHALF is printed.

Example Input/Output 2:
Input: 
zyasnw 

Output:
SECONDHALF

-----------------------------------------------------------------------------------------------------------------

Program: 

string = input()
count1 = 0
count2 = 0
for i in string:
  if i>='a' and i<='m':
    count1+=1
  elif i>='n' and i<='z':
    count2+=1
if count1>count2:
  print("FIRSTHALF")
elif count2>count1:
  print("SECONDHALF")
else:
  print("-1")



