An integer N and a string S are passed as the input to the program. The program must reverse the first N words in S and print the modified S as the output. 

Boundary Condition(s):
2 <= N <= 50 
3 <= Length of S <= 250 

Input Format:
The first line contains N.
The second line contains S.

Output Format: 
The first line contains the modified string. 

Example Input/Output 1:
Input:
3
the pen is mightier than the sword

Output: 
is pen the mightier than the sword 

Explanation:
The first 3 words "the pen is" are reversed and the remaining words are printed as it is.

Example Input/Output 2:
Input:
6 
the squeaky wheel gets the grease 

Output:
grease the gets wheel squeaky the

----------------------------------------------------------------------------------------------------


Program:

IntegerInput = int(input())
StringInput = input().split()
spliting = StringInput[0:IntegerInput][::-1]+StringInput[IntegerInput:]
print(*spliting)



