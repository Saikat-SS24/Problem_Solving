""" Given an array of n positive integers. Find the sum of the maximum sum subsequence of the given array such that 
the integers in the subsequence are sorted in strictly increasing order i.e. a strictly increasing subsequence. 

Example 1:

Input: 
N = 5, arr[] = {1, 101, 2, 3, 100} 
Output: 
106
Explanation:
The maximum sum of a increasing sequence is obtained from {1, 2, 3, 100},
Example 2:

Input: 
N = 4, arr[] = {4, 1, 2, 3}
Output: 
6
Explanation:
The maximum sum of a increasing sequence is obtained from {1, 2, 3}.
Your Task:  
You don't need to read input or print anything. Complete the function maxSumIS() which takes N and array arr as input
parameters and returns the maximum value.

Expected Time Complexity: O(N2)
Expected Auxiliary Space: O(N)

Constraints:
1 ≤ N ≤ 103
1 ≤ arr[i] ≤ 105 """


#User function Template for python3
class Solution:
	def maxSumIS(self, Arr, n):
		# code here
		if n == 0:
            return 0
        dp = [0] * n
        dp[n - 1] = Arr[n - 1]
 
        for i in reversed(range(n - 1)):
            maxSum = 0
            for j in range(i + 1, n):
                if Arr[j] > Arr[i]:
                    maxSum = max(maxSum, dp[j])
            dp[i] = Arr[i] + maxSum
 
        return max(dp)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.maxSumIS(Arr,n)
		print(ans)

# } Driver Code Ends