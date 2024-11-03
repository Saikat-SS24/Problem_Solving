""" There are N points on the road, you can step ahead by 1 or 2 . If you start from a point 0, and can only move from 
point i to point i+1 after taking a step of length one, find the number of ways you can reach at point N. 

Example 1:

Input: 
N = 4
Output: 
5
Explanation: Three ways to reach at 4th
point. They are {1, 1, 1, 1}, {1, 1, 2},
{1, 2, 1} {2, 1, 1}, {2, 2}.

Example 2:

Input: N = 5
Output: 8
Explanation: Three ways to reach at 5th
point. They are {1, 1, 1, 1, 1},
{1, 1, 1, 2}, {1, 1, 2, 1}, {1, 2, 1, 1},
{2, 1, 1, 1}{1, 2, 2}, {2, 1, 2}, {2, 2, 1}
Your Task:
You don't need to read or print anyhting. Your task is to complete the function nthPoint() which takes N as input 
parameter and returns the total number of ways modulo 109 + 7 to reach at Nth point.

Expected Time Complexity: O(N)
Expected Space Complexity: O(N)

Constraints:
1 ≤ N ≤ 105 """


#User function Template for python3

class Solution:
	def nthPoint(self,n):
		# Code here
        mod=(10**9)+7
        fib=[0]*(n+1)
        fib[0]=1
        fib[1]=1
        for i in range(2,n+1):
            fib[i]=(fib[i-1]+fib[i-2])%mod
        return fib[n]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.nthPoint(n)
		print(ans)
# } Driver Code Ends