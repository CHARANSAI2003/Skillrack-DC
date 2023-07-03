The program must accept a string S as the input. The program must print the first character, the third character, the sixth character and so on as the output.

Boundary Condition(s): 
1 <= Length of S <= 100

Input Format: 
The first line contains the string S.

Output Format:
The first line contains the characters of string S as per the given conditions.

Example Input/Output 1: 
Input:
abcdefghijklmno

Output:
acfjo

Explanation:
1st character is a.
3rd character is c.
6th character is f.
10th character is j.
15th character is o. 
So these characters are printed as the output. 

Example Input/Output 2:
Input:
northeastwestsouth

Output:
nrewo

-----------------------------------------------------------------------------------------------------------

Program:

#include<stdio.h>
#include<stdlib.h>

int main()
{
    char a[10001];
    scanf("%s",a);
    int b=0,d=1;
    for(int i=0;i<strlen(a);i++){
        if(strlen(a)>b+i){
        printf("%c",a[b+i]);
        b+=d;
        d+=1;
        }
    }
}
