Implement the function removeIndices(int arr[], int M, int indices[], int N) where arr is an integer array of size M and indices is an integer array of size N. The
function must remove the values from the array arr based on the index given in the indices array. 
Note: Do not print inside the function. The first M-N integers in the array arr will contain the remaining integers after removing the integers. 

Example Input/Output 1:
Input: 
6 3 
1 2 3 4 5 6
1 4 2

Output: 
1 4 6 

Explanation:
The elements at the indices 1 4 2 are 2 5 and 3. 
2 5 and 3 are removed from 1 2 3 4 5 6.
Hence 1 4 6 is printed.

---------------------------------------------------------------------------------

Program:

void removeIndices(int arr[], int M, int indices[], int N)
{
    int n=0;
    int arr1[M];
    for(int i=0;i<M;i++){
        arr1[i]=0;
    }
    for(int i=0;i<N;i++){
        if(indices[i]>=0 && indices[i]<=M){
            arr1[indices[i]]=1;
        }
    }
    for(int i=0;i<M;i++){
        if(!arr1[i]){
            arr[n++]=arr[i];
        }
    }
    M=n;
}
