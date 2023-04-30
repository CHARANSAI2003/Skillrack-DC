The program must accept a string S which contains only lower case alphabets as the input.The program must remove the consonants which are occurred consecutively. 
Then the program must print the modified string S as the output. Note: At least one vowel is always present in the string S. 

Boundary Condition(s):
1 <= Length of S <= 100 

Input Format: 
The first line contains the string S.

Output Format: 
The first line contains the modified string value of S.

Example Input/Output 1:
Input:
elephants

Output:
elea

Explanation: 
The consonants p and h are have occurred consecutively so they are removed from the string "elephants".
Now the string becomes "eleants".
The consonants n t and s are occurred consecutively so they are removed from the string "eleants".
Now the string becomes "elea".
Hence the output is elea

Example Input/Output 2:
Input:
document

Output:
docume

-------------------------------------------------------------------------------------------------------------

Program:

n=input().strip()
m=""
def isVowel(letter):
    if letter=="a" or letter=="e" or letter=="i" or letter=="o" or letter=="u":
        return True 
    return False 
prevVowel = True 
for i in range(len(n)):
    if isVowel(n[i]):
        m+=n[i]
        prevVowel=True 
    else:
        if not prevVowel:
            continue 
        if i+1==len(n):
            m+=n[i]
        else:
            if isVowel(n[i+1]):
                m+=n[i]
                prevVowel=True 
            else:
                prevVowel=False
print(m)                

