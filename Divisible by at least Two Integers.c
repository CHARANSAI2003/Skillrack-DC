The program must accept four integers N, A, B and C as the input. The program must print the integers from 1 to N which are divisible by at least two integers among 
A, B and C as the output. 

Boundary Condition(s): 
1 <= N <= 10^8 
1 <= A, B, C <= N 

Input Format:
The first line contains the values of N, A, B and C separated by a space.

Output Format:
The first line contains the integers from 1 to N which are divisible by at least two integers among A, B and C separated by a space.

Example Input/Output 1: 
Input: 
10 2 3 4

Output:
4 6 8 

Explanation:
4 is divisible by both 2 and 4.
6 is divisible by both 2 and 3.
8 is divisible by both 2 and 4.
So these integers are divisible by at least two integers among 2, 3 and 4. 
Hence the output is 4 6 8 

Example Input/Output 2:
Input:
80 12 5 7 

Output:
35 60 70

----------------------------------------------------------------------------------------------------------------

Program:

#include<stdio.h>
#include<stdlib.h>

int main()
{
    int a,b,c,d;
    scanf("%d%d%d%d",&a,&b,&c,&d);
    for(int i=1;i<=a;i++){
        if(i%b==0 && i%c==0){
            printf("%d ",i);
        }
        else if(i%b==0 && i%d==0){
            printf("%d ",i);
        }
        else if(i%c==0 && i%d==0){
            printf("%d ",i);
        }
    }
}

