The program must accept four integers N, X, Y and Z as the input. The program must print the first N integers which are only divisible by X or Y or Z as the output.

Boundary Condition(s): 
1 <= N, X, Y, Z <= 1000

Input Format:
The first line contains four integers N, X, Y and Z separated by space(s). 

Output Format:
The first line contains the first N integers which are only divisible by X or Y or Z separated by a space.

Example Input/Output 1:
Input:
10 5 7 3

Output: 
3 5 6 7 9 10 12 14 18 20

Explanation:
3 is only divisible by 3.
5 is only divisible by 5.
6 is only divisible by 3. 
7 is only divisible by 7.
9 is only divisible by 3.
10 is only divisible by 5.
12 is only divisible by 3.
14 is only divisible by 7.
18 is only divisible by 3.
20 is only divisible by 5.
Hence the output is 3 5 6 7 9 10 12 14 18 20

Example Input/Output 2:
Input:
5 9 2 7

Output:
2 4 6 7 8

---------------------------------------------------------------------------------------------------------------------------------

Program:

#include<stdio.h>
#include<stdlib.h>

int main()
{
    int a,b,c,d;
    scanf("%d%d%d%d",&a,&b,&c,&d);
    int e=0,f=1,k=0;
    while(e<a){
        if(f%b==0 || f%c==0 || f%d==0){
            if(f%b==0 && f%c==0){
                k=0;
            }
            else if(f%b==0 && f%d==0){
                k=0;
            }
            else if(f%c==0 && f%d==0){
                k=0;
            }
            else{
                printf("%d ",f);
                e++;
            }
        }
        f++;
    }
}
