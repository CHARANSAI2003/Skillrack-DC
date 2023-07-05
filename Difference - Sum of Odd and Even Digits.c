Given a maximum of hundred digits as the input. The program must print the difference between the sum of odd and even digits as the output. If the input is not a valid
number, then print Invalid as the output.

Example Input/Output 1:
Input:
118745913

Output:
15

Explanation: 
The sum of odd digits is 27 (1, 1, 7, 5, 9, 1 and 3).
The sum of even digits is 12 (8 and 4).
So the difference is 27-12 = 15.
Hence the output is 15

Example Input/Output 2:
Input:
235468173645

Output: 
-6

Example Input/Output 3: 
Input:
76320Afk384

Output: 
Invalid

Note:
The invalid number may contain white spaces.

---------------------------------------------------------------------------------------------------

Program:

#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>

int main()
{
    char a[1001];
    scanf("%[^\n]",a);
    int b=0,c=0,d=0;
    for(int i=0;i<strlen(a);i++){
        if(isdigit(a[i])==0 || isspace(a[i])){
            d++;
            break;
        }
        else if(a[i]%2==0){
            b=b+(a[i]-'0');
        }
        else if(a[i]%2==1){
            c+=(a[i]-'0');
        }
    }
    if(d>0){
        printf("Invalid");
    }
    else{
        printf("%d",(c-b));
    }
}

