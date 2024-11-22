""" Given an array prices[] of length n, representing the prices of the stocks on different days. The task is to find 
the maximum profit possible by buying and selling the stocks on different days when at most one transaction is allowed. 
Here one transaction means 1 buy + 1 Sell. If it is not possible to make a profit then return 0.

Note: Stock must be bought before being sold.

Examples:

Input: prices[] = [7, 10, 1, 3, 6, 9, 2]
Output: 8
Explanation: You can buy the stock on day 2 at price = 1 and sell it on day 5 at price = 9. Hence, the profit is 8.

Input: prices[] = [7, 6, 4, 3, 1]
Output: 0 
Explanation: Here the prices are in decreasing order, hence if we buy any day then we cannot sell it at a greater 
price. Hence, the answer is 0.

Input: prices[] = [1, 3, 6, 9, 11]
Output: 10 
Explanation: Since the array is sorted in increasing order, we can make maximum profit by buying at price[0] and 
selling at price[n-1].

Constraint:
1 <= prices.size()<= 105
0 <= prices[i] <=104  """


class Solution:
    def maximumProfit(self, prices):
        # code here
        minSoFar = prices[0]
        res = 0
        # Update the minimum value seen so far 
        # if we see smaller
        for i in range(1, len(prices)):
            minSoFar = min(minSoFar, prices[i])
            # Update result if we get more profit                
            res = max(res, prices[i] - minSoFar)
        
        return res


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())  # Read number of test cases
    for _ in range(t):
        # Read input and split it into a list of integers
        prices = list(map(int, input().split()))
        # Create a Solution object and calculate the result
        obj = Solution()
        result = obj.maximumProfit(prices)
        # Print the result
        print(result)

# } Driver Code Ends