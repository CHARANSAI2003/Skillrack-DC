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
1 2 3 4 
2 * * 3 
3 * * 2
4 3 2 1

Example Input/Output 2:
Input:
5

Output:
1 2 3 4 5 
2 * * * 4
3 * * * 3
4 * * * 2
5 4 3 2 1


------------------------------------------------------------------------------------------------------------------------------

Program:

#include <iostream>
 
using namespace std;

int main()
{
    int num1;
    cin >> num1;
    int f1=2,l1=num1-1;
    for(int i=1;i<=num1;i++){
        for(int j=1;j<=num1;j++){
            if(i==1){
                cout << j << " ";
            }
            else if(i==num1){
                cout << num1-(j-1)<< " ";
            }else if(j==1){
                cout << f1 << " ";
                f1++;
            }
            else if(j==num1){
                cout<<l1<<" ";
                l1--;
            }
            else{
                cout<<"* ";
            }
        }
        cout<<endl;
    }
    return 0;

}

