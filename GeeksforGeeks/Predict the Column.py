""" Given a matrix(2D array) M of size N*N consisting of 0s and 1s only. The task is to find the column with maximum 
number of 0s. If more than one column exists, print the one which comes first. If the maximum number of 0s is 0 then 
return -1.

Example:

Input:
N = 3
M[][] = {{0, 0, 0},
          {1, 0, 1},
          {0, 1, 1}}
          
Output:
0
Explanation:
0th column (0-based indexing) is having 2 zeros which is maximum among all columns and comes first.
Your Task:
Your task is to complete the function columnWithMaxZero() which should return the column number with the maximum number
of zeros. 

Expected Time Complexity: O(N * N)
Expected Auxiliary Space: O(1)

Constraints:
1 <= N <= 103
0 <= A[i][j] <= 1 """


#User function Template for python3

class Solution:
    def columnWithMaxZeros(self,arr,N):
        # code here
        res = []
        cnt = 0
        for i in range(N):
            for j in range(N):
                if arr[j][i] == 0:
                    cnt += 1
            res.append(cnt)
            cnt = 0
        if sum(res) == 0:
            return -1
        else:
            return res.index(max(res))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = []
        for i in range(N):
            line = [int(x) for x in input().strip().split()]
            arr.append(line)
        ob=Solution()
        print(ob.columnWithMaxZeros(arr,N))


# } Driver Code Ends