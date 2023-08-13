""" Given a positive integer n, find the nth fibonacci number. Since the answer can be very large, return the answer modulo 1000000007.

Example 1:

Input: 
n = 2
Output: 
1 
Explanation: 
1 is the 2nd number of fibonacci series.
Example 2:

Input: 
n = 5
Output: 
5
Explanation: 
5 is the 5th number of fibonacci series. """


class Solution:
    def nthFibonacci(self, n : int) -> int:
        # code here
        if n<=1:
            return n
        fibonacci = [0] * (n+1)
        fibonacci[1] = 1
        
        for i in range(2,n+1):
            fibonacci[i] = (fibonacci[i - 1] + fibonacci[i - 2]) % 1000000007
        return fibonacci[i]


#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.nthFibonacci(n)
        
        print(res)
        

# } Driver Code Ends