The program must accept the original price P and the discounted price D of N items as the input. The program must print the discounted price of the item having the maximum
discount amount. If more than one items are having the maximum discount amount then print the discounted price of the cheapest item among them. 

Boundary Condition(s):
2 <= N <= 100 
1 <= P, D <= 10^7 

Input Format:
The first line contains the value of N. The next N lines each contain the values of P followed by D separated by a space.

Output Format:
The first line contains the discounted price based on the given conditions. 

Example Input/Output 1:
Input: 
4
100 90
500 450
100 1 
160 100

Output:
1

Explanation:
Discount Amount = Original Price - Discounted Price 
For the 1st item, the discount amount is 10 (100 - 90). 
For the 2nd item, the discount amount is 50 (500 - 450).
For the 3rd item, the discount amount is 99 (100 - 1).
For the 4th item, the discount amount is 60 (160 - 100).
The 3rd item is having more discount than others. So the discounted amount for the 3rd item is printed.

Example Input/Output 2:
Input:
3
10 2
1000 999
100 92

Output: 
2

-----------------------------------------------------------------------------------------

Program:
  
n=int(input())
a1=[]
a2=[]
for i in range(n):
    a,b=list(map(int,input().split()))
    c=a-b 
    a1.append(c)
    a2.append(b)
max_a1=max(a1)
a3=[]
for i in range(len(a1)):
    if max_a1 <= a1[i]:
        a3.append(a2[i])
print(min(a3))

