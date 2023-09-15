""" Given an array arr[] of size N, check if it can be partitioned into two parts such that the sum of elements 
in both parts is the same.

Example 1:

Input: N = 4
arr = {1, 5, 11, 5}
Output: YES
Explanation: 
The two parts are {1, 5, 5} and {11}.
Example 2:

Input: N = 3
arr = {1, 3, 5}
Output: NO
Explanation: This array can never be 
partitioned into two such parts.
Your Task:
You do not need to read input or print anything. Your task is to complete the function equalPartition() which takes the value N and the array as input parameters and returns 1 if the partition is possible. Otherwise, returns 0.

Expected Time Complexity: O(N*sum of elements)
Expected Auxiliary Space: O(N*sum of elements)

Constraints:
1 ≤ N ≤ 100
1 ≤ arr[i] ≤ 1000
N*sum of elements ≤ 5*106 """


# User function Template for Python3

class Solution:
    def equalPartition(self, N, arr):
        # code here
        s = sum(arr)
        if s%2 == 1:
            return 0
        else:
            target = s//2
            
        # initialization for dynamic programming
		dp = [[0]*(target+1) for _ in range(N+1)]
		dp[0] = [1]+[0]*target
		
		# recursive scheme, stop if target is achieved
		i = 1
		while i<N:
		    for j in range(target+1):
		        if j >= arr[i-1]:
		            dp[i][j] = dp[i-1][j]+dp[i-1][j-arr[i-1]]
		        else:
		            dp[i][j] = dp[i-1][j]
		    if dp[i][target]>0:
		        return 1
		    i = i+1
		
		return 0

#{ 
 # Driver Code Starts
# Initial Template for Python3

import sys
input = sys.stdin.readline
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])
        
        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")
# } Driver Code Ends