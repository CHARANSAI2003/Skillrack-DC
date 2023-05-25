The program must accept an integer N as the input. The program must print the desired pattern as shown in the Example Input/Output section. 

Boundary Condition(s):
1 <= N <= 1000

Input Format:
The first line contains the integer N.

Output Format:
The first N lines contain the desired pattern as shown in the Example Input/Output section. 

Example Input/Output 1:
Input:
4

Output:
1
2*3
4*5*6
7*8*9*10 

Example Input/Output 2: 
Input:
7

Output:
1
2*3
4*5*6
7*8*9*10
11*12*13*14*15 
16*17*18*19*20*21
22*23*24*25*26*27*28

-------------------------------------------------------------------------------------------------------------

Program:

#include<stdio.h>
#include<stdlib.h>

int main()
{
    int n;
    scanf("%d",&n);
    int c=1;
    for(int i=1;i<=n;i++){
        for(int j=0;j<i;j++){
            if(j==(i-1)){
                printf("%d ",c);
            }
            else{
                printf("%d",c);
                printf("*");
            }
            c++;
        }
        printf("\n");
    }
}

