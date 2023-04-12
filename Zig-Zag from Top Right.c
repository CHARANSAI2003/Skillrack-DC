The program must accept an integer N as the input. The program must print the desired pattern as shown in the Example Input/Output section. 

Boundary Condition(s):
1 <= N <= 50

Input Format: 
The first line contains the value of N.

Output Format:
The first N lines containing the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
Input:
4

Output:
4 3 2 1
5 6 7 8
12 11 10 9
13 14 15 16

Example Input/Output 2:
Input:
3

Output:
3 2 1
4 5 6
9 8 7

------------------------------------------------------------------------------------------------------------

Program:

#include <stdio.h>

int main()
{
    int n;
    scanf("%d",&n);
    int k=0;
    for(int i=1;i<=n;i++){
        if(i%2==1){
            k=k+n;
        for(int j=1;j<=n;j++){
            printf("%d ",k);
            k--;
        }
        }
        else{
            k=k+n+1;
            for(int j =1;j<=n;j++){
                printf("%d ",k);
                k++;
            }
            k--;
        }
        printf("\n");
    }
}
