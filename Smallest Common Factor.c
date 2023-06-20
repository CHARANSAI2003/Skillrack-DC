The program must accept two positive integers N1 and N2 as the input. The program must print the smallest common factor of N1 and N2 which is greater than 1 as the output.
If there is no common factor other than 1 then the program must print -1 as the output.

Boundary Condition(s):
2 <= N1,
N2 <= 10^8 

Input Format:
The first line contains the values of N1 and N2 separated by space(s).

Output Format:
The first line contains the common factor.

Example Input/Output 1:
Input: 
15 30

Output:
3

Explanation:
3 is the smallest number (greater than 1) which divides both 15 and 30.
Hence 3 is printed.

Example Input/Output 2:
Input:
3 7

Output:
-1

-------------------------------------------------------------------------------------------------------------------

Program:

#include<stdio.h>
#include<stdlib.h>

int main()
{
    int n,m;
    scanf("%d%d",&n,&m);
    int a=-1;
    for(int i=2;i<m;i++){
        if(n%i==0 && m%i==0){
            a=i;
            break;
        }
    }
    printf("%d",a);
}

