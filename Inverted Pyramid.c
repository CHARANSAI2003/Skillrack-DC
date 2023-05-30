The program must accept an integer N as the input. The program must print the desired pattern as shown in the Example Input/Output section. 

Boundary Condition(s): 
2 <= N <= 100

Input Format:
The first line contains the integer N.

Output Format:
The first N lines contain the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
Input:
4

Output:
1 2 3 4 3 2 1 
* 2 3 4 3 2
* * 3 4 3
* * * 4

Example Input/Output 2: 
Input: 
5

Output:
1 2 3 4 5 4 3 2 1
* 2 3 4 5 4 3 2 
* * 3 4 5 4 3 
* * * 4 5 4
* * * * 5

---------------------------------------------------------------------------------------------

Program:

#include<stdio.h>
#include<stdlib.h>

int main()
{
    int n;
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        int k=1;
        if(i!=0){
            for(int j=0;j<i;j++){
                printf("* ");
                k++;
            }
        }
        if(i!=0 || i==0){
            for(int j=0;j<n-i;j++){
                printf("%d ",k);
                k++;
            }
            k=k-2;
            for(int j=0;j<n-1-i;j++){
                printf("%d ",k);
                k--;
            }
        }
        printf("\n");
    }
}

