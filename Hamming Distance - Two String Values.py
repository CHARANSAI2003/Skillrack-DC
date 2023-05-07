The program must accept two string values S1 and S2 of equal length as the input. The program must print the Hamming distance of two string values as the output.
The Hamming distance of two string values is the minimum number of substitutions required to change one string into the other string value. 

Boundary Condition(s): 
1 <= Length of S1 and S2 <= 1000 

Input Format:
The first line contains S1. 
The second line contains S2.

Output Format:
The first line contains the Hamming distance of S1 and S2. 

Example Input/Output 1:
Input:
karolin
kathrin

Output:
3

Explanation: 
The three characters in karolin or kathrin can be substituted to get the other string value. 
Hence 3 is printed.

Example Input/Output 2:
Input: 
carpet
carrot

Output:
2

--------------------------------------------------------------------------------------------------------

Program:

first_string = input().strip()
second_string = input().strip()
count_not_matched_letter = 0
for i in range(len(first_string)):
    if first_string[i]!=second_string[i]:
        count_not_matched_letter += 1
print(count_not_matched_letter)  

