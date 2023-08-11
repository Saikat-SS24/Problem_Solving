""" You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

 

Example 1:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:

Input: amount = 10, coins = [10]
Output: 1
 

Constraints:

1 <= coins.length <= 300
1 <= coins[i] <= 5000
All the values of coins are unique.
0 <= amount <= 5000 """

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N=len(coins)
        table = [[0 for x in range(N)] for x in range(amount+1)]
     
        # Fill the entries for 0 value case (n = 0)
        for i in range(N):
            table[0][i] = 1
     
        # Fill rest of the table entries in bottom up manner
        for i in range(1, amount+1):
            for j in range(N):
     
                # Count of solutions including coins[j]
                x = table[i - coins[j]][j] if i-coins[j] >= 0 else 0
     
                # Count of solutions excluding coins[j]
                y = table[i][j-1] if j >= 1 else 0
     
                # total count
                table[i][j] = x + y
     
        return table[amount][N-1]