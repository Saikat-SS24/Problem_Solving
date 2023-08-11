""" Given an integer array coins[ ] of size N representing different denominations of currency and an integer sum, find the number of ways you can make sum by using different combinations from coins[ ].  
Note: Assume that you have an infinite supply of each type of coin. And you can use any coin as many times as you want.

Example 1:

Input:
N = 3, sum = 4
coins = {1,2,3}
Output: 4
Explanation: Four Possible ways are: {1,1,1,1},{1,1,2},{2,2},{1,3}.
Example 2:

Input:
N = 4, Sum = 10
coins = {2,5,3,6}
Output: 5
Explanation: Five Possible ways are: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. """


#User function Template for python3

class Solution:
    def count(self, coins, N, Sum):
        # code here 
        # We need sum+1 rows as the table is constructed
        # in bottom up manner using the base case 0 value
        # case (sum = 0)
        table = [[0 for x in range(N)] for x in range(Sum+1)]
     
        # Fill the entries for 0 value case (n = 0)
        for i in range(N):
            table[0][i] = 1
     
        # Fill rest of the table entries in bottom up manner
        for i in range(1, Sum+1):
            for j in range(N):
     
                # Count of solutions including coins[j]
                x = table[i - coins[j]][j] if i-coins[j] >= 0 else 0
     
                # Count of solutions excluding coins[j]
                y = table[i][j-1] if j >= 1 else 0
     
                # total count
                table[i][j] = x + y
     
        return table[Sum][N-1]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        sum,N = list(map(int, input().strip().split()))
        coins = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(coins,N,sum))

# } Driver Code Ends