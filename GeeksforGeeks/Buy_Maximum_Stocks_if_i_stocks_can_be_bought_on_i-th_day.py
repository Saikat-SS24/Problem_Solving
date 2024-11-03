""" In a stock market, there is a product with its infinite stocks. The stock prices are given for N days, where 
price[i] denotes the price of the stock on the ith day.
There is a rule that a customer can buy at most i stock on the ith day.
If the customer has an amount of k amount of money initially. The task is to find out the maximum number of stocks a 
customer can buy. 

Example 1:

Input:
price = [10,7,19]
k = 45
Output: 
4
Explanation: 
A customer purchases 1 stock on day 1, 2 stocks on day 2 and 1 stock on day 3 for 10, 7 * 2 = 14 and 19 respectively. 
Hence, total amount is 10 + 14 + 19 = 43 and number of stocks purchased is 4.

Example 2:

Input: 
price = [7,10,4]
k = 100
Output: 
6
Explanation:
Buy on all 3 days.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function buyMaximumProducts() which takes 
an array price and an integer k and returns an integer as output.

Expected Time Complexity: O(NlogN)
Expected Auxiliary Space: O(N)

Constraints:
1 <= N <= 104
1 <= price[i] <= 104
1 <= k <= 104 """


from typing import List

from typing import List
class Solution:
    def buyMaximumProducts(self, n : int, k : int, price : List[int]) -> int:
        # code here
        ans = 0
        for i, x in sorted(enumerate(price), key=lambda a: a[1]):
            buy = min(k // x, i + 1)
            if buy == 0:
                break
            ans += buy
            k -= buy * x
        return ans



#{ 
 # Driver Code Starts


class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n,k = map(int,input().strip().split())
        
        price=IntArray().Input(n)
        
        obj = Solution()
        res = obj.buyMaximumProducts(n, k, price)
        
        print(res)     

# } Driver Code Ends