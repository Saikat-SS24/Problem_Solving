""" Given an sorted array A of size N. Find number of elements which are less than or equal to given element X.

Example 1:

Input:
N = 6
A[] = {1, 2, 4, 5, 8, 10}
X = 9
Output:
5
 
Example 2:

Input:
N = 7
A[] = {1, 2, 2, 2, 5, 7, 9}
X = 2
Output:
4
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function countOfElements() which takes 
the array A[], its size N and an integer X as inputs and returns the number of elements which are less than or equal 
to given element.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 <= N <= 105
1 <= Ai <= 105
0 <= X <= 105 """ 

#User function Template for python3

def countOfElements( a, n, x):
    count = 0
    for i in range(n):
        if(a[i] <= x):
            count = count+1
    return count




#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        print(countOfElements(a, n, k))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends