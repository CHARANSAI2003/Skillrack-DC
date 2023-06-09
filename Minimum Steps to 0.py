The program must accept two integers N and K as the input. The program must print the minimum number of steps required to reach 0 from N based on the following steps. 
-If N is divisible by K then divide N by k. 
-If N is not divisible by K then decrement N by 1.

Boundary Condition(s):
1 <= N <= 10^18 
2 <= K <= 10^18

Input Format:
The first line contains the values of N and K separated by a space.

Output Format:
The first line contains the minimum number of steps required to reach 0 from N.

Example Input/Output 1:
Input:
29 3 

Output: 
6

Explanation: 
29 -> 28 -> 27 -> 9 -> 3 -> 1 -> 0

Example Input/Output 2:
Input:
31 2

Output:
9

----------------------------------------------------------------------------------------------

Program:

n,k=list(map(int,input().split()))
count = 0
while n>0:
    if n%k==0:
        n//=k 
        count+=1
    else:
        count+=n%k 
        n-=n%k
print(count)    


