""" Given an array of integers, your task is to find the smallest and second smallest element in the array. If smallest 
and second smallest do not exist, print -1.

Example 1:

Input :
5
2 4 3 5 6
Output :
2 3 
Explanation: 
2 and 3 are respectively the smallest 
and second smallest elements in the array.

Example 2:

Input :
6
1 2 1 3 6 7
Output :
1 2 
Explanation: 
1 and 2 are respectively the smallest 
and second smallest elements in the array.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function minAnd2ndMin() which takes the 
array A[] and its size N as inputs and returns a vector containing the smallest and second smallest element if 
possible, else return {-1,-1}.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1<=N<=105
1<=A[i]<=105 """#User function Template for python3

def minAnd2ndMin( a, n):
    #code here
    res = sorted(list(set(a)))
    if len(res) >= 2:
        return [res[0],res[1]]
    else:
        return [-1,-1]




#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        
        product = minAnd2ndMin(a, n)
        if product[0]==-1:
            print(product[0])
        else:
            print(product[0], end=" ")
            print(product[1])

        T -= 1


if __name__ == "__main__":
    main()    
# } Driver Code Ends