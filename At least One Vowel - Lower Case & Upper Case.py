The program must accept a string S as the input. The program must print YES if the string S contains at least one lower case vowel and at least one upper case vowel.
Else the program must print NO as the output.

Boundary Condition(s):
2 <= Length of S <= 100

Input Format:
The first line contains S.

Output Format:
The first line contains either YES or NO.

Example Input/Output 1:
Input:
Engineering

Output: 
YES

Explanation: 
The upper case vowel in the string "Engineering" is E.
The lower case vowels in the string "Engineering" are i, e, e and i. 
Here both the upper case and lower case vowels are present at least once in the string.
So YES is printed as the output.

Example Input/Output 2:
Input:
Computer

Output:
NO

----------------------------------------------------------------------------------------------------------------

Program:

String = input().strip()
captial_Vowels = "AEIOU"
small_letters_Vowels = "aeiou"
count_captial_vowels,count_small_letters_vowels = 0,0
for i in String:
    if i in captial_Vowels:
        count_captial_vowels += 1
    elif i in small_letters_Vowels:
        count_small_letters_vowels += 1
if count_captial_vowels != 0 and count_small_letters_vowels != 0:
    print("YES")
else:
    print("NO")

