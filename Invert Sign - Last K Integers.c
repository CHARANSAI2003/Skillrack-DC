The program must accept N integers and an integer K as the input. The program must invert the sign of the last K integers among the N integers. Then the program must print 
the modified values of N integers as the output. 

Boundary Condition(s): 
1 <= N <= 1000 
1 <= K <= N 

Input Format: 
The first line contains N.
The second line contains N integers separated by space(s).
The third line contains K.

Output Format:
The first line contains the modified values of N integers separated by a space.

Example Input/Output 1: 
Input:
5 
20 40 56 -50 -40
3

Output:
20 40 -56 50 40 

Explanation: 
The last three integers are 56 -50 and -40.
Then invert the sign of those integers as -56 50 and 40.
Hence the output is 20 40 -56 50 40 

Example Input/Output 2:
Input:
7
30 83 48 61 55 48 58 
7

Output:
-30 -83 -48 -61 -55 -48 -58

---------------------------------------------------------------------------------------------------------------

Program:

#include<stdio.h>
#include<stdlib.h>

int main()
{
    int a;
    scanf("%d",&a);
    int b[a];
    for(int i=0;i<a;i++){
        scanf("%d",&b[i]);
    }
    int c;
    scanf("%d",&c);
    for(int i=0;i<a;i++){
        if((n-c)<i){
            printf("%d ",(b[i]-(b[i]*2)));
        }
        else{
            printf("%d ",b[i]);
        }
    }
    
}
