""" Given an array of integers cost[] where cost[i] is the cost of the ith step on a staircase. Once the cost is paid, 
you can either climb one or two steps. Return the minimum cost to reach the top of the floor.
Assume 0-based Indexing. You can either start from the step with index 0, or the step with index 1.

Examples:

Input: cost[] = [10, 15, 20]
Output: 15
Explanation: Cheapest option is to start at cost[1], pay that cost, and go to the top.

Input: cost[] = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest option is to start on cost[0], and only step on 1s, skipping cost[3].

Constraints:
2 ≤ cost.size() ≤ 105
0 ≤ cost[i] ≤ 999  """


#Back-end complete function Template for Python 3

class Solution:
    def minCostClimbingStairs(self, cost):
        #Write your code here
        n = len(cost)
        if n == 1:
            return cost[0]
    
        prev2 = cost[0]
        prev1 = cost[1]
        
        for i in range(2, n):
            curr = cost[i] + min(prev1, prev2)
            prev2 = prev1
            prev1 = curr

        return min(prev1, prev2)


#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))  # Input array
    obj = Solution()
    res = obj.minCostClimbingStairs(arr)
    print(res)
    print("~")

# } Driver Code Ends