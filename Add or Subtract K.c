The program must accept N integers and an integer K as the input. For each integer I among the N integers, the program must add K to I if the unit digit of I and K are
equal. Else the program must subtract K from I. Then the program must print the modified integers as the output.

Boundary Condition(s): 
1 <= N <= 100 
1 <= Each integer value, K <= 10^7

Input Format:
The first line contains N and K separated by a space.
The first line contains N integers separated by a space.

Output Format: 
The first line contains the modified N integers. 

Example Input/Output 1:
Input: 
4 32 
22 154 12 11

Output:
54 122 44 -21

Explanation: 
The unit digit of 22 and 32 are equal so they are added and printed 22 + 32 = 54.
The unit digit of 154 and 32 are not equal so they are subtracted and printed 154 - 32 = 122.
The unit digit of 12 and 32 are equal so they are added and printed 12 + 32 = 44.
The unit digit of 11 and 32 are not equal so they are subtracted and printed 11 - 32 = -21.

Example Input/Output 2:
Input:
6 27
17 500 27 37 106 107 

Output:
44 473 54 64 79 134

-------------------------------------------------------------------------------------------------------------------------------------------

Program:

#include<stdio.h>
#include<stdlib.h>

int main()
{
    int a,b;
    scanf("%d%d",&a,&b);
    int z[a];
    for(int i=0;i<a;i++){
        scanf("%d",&z[i]);
    }
    for (int i=0;i<a;i++){
        if(z[i]%10==b%10){
            printf("%d ",z[i]+b);
        }
        else{
            printf("%d ",z[i]-b);
        }
    }
}
