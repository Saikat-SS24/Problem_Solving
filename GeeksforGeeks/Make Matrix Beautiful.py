""" A beautiful matrix is a matrix in which the sum of elements in each row and column is equal. Given a square matrix of size NxN. Find the minimum number of operation(s) that are required to make the matrix beautiful. In one operation you can increment the value of any one cell by 1.
Example 1:

Input:
N = 2
matrix[][] = {{1, 2},
              {3, 4}}
Output: 
4
Explanation:
Updated matrix:
4 3
3 4
1. Increment value of cell(0, 0) by 3
2. Increment value of cell(0, 1) by 1
Hence total 4 operation are required.
Example 2:

Input:
N = 3
matrix[][] = {{1, 2, 3},
              {4, 2, 3},
              {3, 2, 1}}
Output: 
6
Explanation:
Number of operations applied on each cell are as follows:
1 2 0
0 0 0
0 1 2
Such that all rows and columns have sum of 9.
Your Task: 
You don't need to read input or print anything. Complete the function findMinOpeartion() that takes matrix and n as input parameters and returns the minimum number of operations.

Expected Time Complexity: O(N * N)
Expected Auxiliary Space: O(N)

Constraints:
1 <= N <= 103
1 <= matrix[i][j] <= 106 """

#User function Template for python3

class Solution:
    def findMinOpeartion(self, matrix, n):
        # Code here
        # initialize the sumRow[] and sumCol[] array to 0
        sumRow=[0]*n
        sumCol=[0]*n
        # calculate sumRow[] and sumCol[] array
        for i in range(n):
            for j in range(n):
                sumRow[i]+=matrix[i][j]
                sumCol[j]+=matrix[i][j]
        # find maximum sum value in either row or in column
        
        maxSum=0
        for i in range(n):
            maxSum=max(maxSum, sumRow[i])
            maxSum=max(maxSum, sumCol[i])
        
        count=0
        i=0
        j=0
        while i<n and j<n:
            # find minimum increment required in either row or column
            diff=min(maxSum-sumRow[i],maxSum-sumCol[j])
            matrix[i][j]+=diff
            sumRow[i]+=diff
            sumCol[i]+=diff
            # update the count variable
            count+=diff
            # if ith row satisfied, increment ith value for the next iteration
            if(sumRow[i]==maxSum):
                i+=1
            # if jth column satisfied, increment jth value for the next iteration
            if(sumCol[j]==maxSum):
                j+=1
                
        return count
        
    # utility function to print the matrix
    def printMatrix(matrix, n):
        for i in range(n):
            for j in range(n):
                print(matrix[i][j], end=" ")
            print()
        

#{ 
 # Driver Code Starts

#Initial Template for Python 3

for _ in range(int(input())):
    n = int(input())
    matrix = [list(map(int,input().split())) for _ in range(n)]
    ob = Solution()
    print(ob.findMinOpeartion(matrix, n))
# } Driver Code Ends