""" You are given an integer n, return the fibonacci series till the nth(0-based indexing) term. Since the terms can
become very large return the terms modulo 109+7.

Example 1:

Input:
n = 5
Output:
0 1 1 2 3 5
Explanation:
0 1 1 2 3 5 is the Fibonacci series up to the 5th term.

Example 2:

Input:
n = 10
Output:
0 1 1 2 3 5 8 13 21 34 55
Explanation:
0 1 1 2 3 5 8 13 21 34 55 is the Fibonacci series up to the 10th term.
Your Task:
You don't need to read input or print anything. Your task is to complete the function Series() which takes an Integer 
n as input and returns a Fibonacci series up to the nth term.

Expected Time Complexity: O(n)
Expected Space Complexity: O(n)

Constraint:
1 <= n <= 105  """


#User function Template for python3

class Solution:
    def series(self, n):
        # Code here
        res = [0,1]
        for i in range(2,n+1):
            x = res[-1]+res[-2]
            res.append(x%(10**9+7))
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        result = ob.series(N)
        print(*result)
# } Driver Code Ends