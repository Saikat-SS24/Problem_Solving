""" Given a fence with n posts and k colors, find out the number of ways of painting the fence so that not more than 
two consecutive posts have the same colors. Since the answer can be large return it modulo 109 + 7.

Example 1:

Input:
n = 3
k = 2 
Output: 6
Explanation: 
We have following possible combinations:

Example 2:

Input:
n = 2
k = 4 
Output: 16
Explanation: 
After coloring first post with
4 possible combinations, you can still color
next posts with all 4 colors. Total possible 
combinations will be 4x4=16
Your Task:
Since, this is a function problem. You don't need to take any input or print anything, as it is already accomplished by 
the driver code. You just need to complete the function countWays() that takes n and k as parameters and returns the 
number of ways in which the fence can be painted (modulo 109 + 7).

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 ≤ N ≤ 5000
1 ≤ K ≤ 100 """


#User function Template for python3

class Solution:
    def countWays(self,n,k):
        #code here
        MOD = 1000000007
        # If there are no posts, there is 0 way to paint the fence.
        if n == 0:
            return 0
        # If there is only one post, there are k ways to paint it.
        if n == 1:
            return k
        # Initialize the dp array with 0 for 0 and 1 post.
        dp = [0] * (n + 1)
        dp[1] = k
        dp[2] = k * k
        # Fill the dp array using the recurrence relation.
        for i in range(3, n + 1):
            dp[i] = (dp[i - 1] * (k - 1) + dp[i - 2] * (k - 1)) % MOD
        
        return dp[n]



#{ 
 # Driver Code Starts

#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    x=list(map(int,input().split()))
    n=x[0]
    k=x[1]
    ob = Solution()
    ans=ob.countWays(n,k)
    print(ans)

# } Driver Code Ends