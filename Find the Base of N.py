The program must accept a string N as the input. The program must print the output based on the following conditions. 
- If N is a valid binary representation then print "Binary" as the output. 
- Else if N is a valid octal representation then print "Octal" as the output. 
- Else if N is a valid decimal representation then print "Decimal" as the output.
- Else if N is a valid hexadecimal representation then print "Hexadecimal" as the output.
- Else the program must print "Invalid" as the output. Note: The alphabets in N are only in upper case.

Boundary Condition(s):
1 <= Length of N <= 100

Input Format:
The first line contains the string N.

Output Format: 
The first line contains the string value based on the conditions mentioned above.

Example Input/Output 1:
Input: 
110

Output 
Binary

Explanation: 
110 is the valid binary, octal, decimal and hexadecimal representations.
But in the mentioned order, Binary comes first.
Hence the output is Binary 

Example Input/Output 2:
Input:
62067 

Output:
Octal

Explanation: 
62067 is the valid octal, decimal and hexadecimal representations. 
But in the mentioned order, Octal comes first. 
Hence the output is Octal 

Example Input/Output 3:
Input:
10G 

Output:
Invalid

-----------------------------------------------------------------------------------------------------------------

Program:

n=input().strip()

def bin(n):
    a=['0','1']
    for i  in n:
        if i not in a:
            return 1
    return 0    

def oct(n):
    a=['0','1','2','3','4','5','6','7']
    for i  in n:
        if i not in a:
            return 1
    return 0    

def dec(n):
    a=['0','1','2','3','4','5','6','7','8','9']
    for i  in n:
        if i not in a:
            return 1
    return 0

def hex(n):
    a=['A','B','C','D','E','F','a','b','c','d','e','f','0','1','2','3','4','5','6','7','8','9']
    for i  in n:
        if i not in a:
            return 1
    return 0      
    

if bin(n)==0:
    print("Binary")
elif oct(n)==0:
    print("Octal")
elif dec(n)==0:
    print("Decimal")
elif hex(n)==0:
    print("Hexadecimal")
else:
    print("Invalid")
    
