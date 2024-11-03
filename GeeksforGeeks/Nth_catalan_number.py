""" Given a number N. The task is to find the Nth catalan number.
The first few Catalan numbers for N = 0, 1, 2, 3, … are 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, …

Catalan Number for N is equal to the number of expressions containing N pairs of paranthesis that are correct matched, i.e., for each of the N '(' there exist N ')' on there right and vice versa.

Since answer can be huge return answer modulo 1e9+7.

Note: Positions start from 0 as shown above.

Example 1:

Input:
N = 5
Output: 42
Example 2:

Input:
N = 4
Output: 14
Your Task:
Complete findCatalan() function that takes n as an argument and returns the Nth Catalan number. The output is printed by the driver code.

Expected Time Complexity: O(N^2).
Expected Auxiliary Space: O(N).

Constraints:
1 <= N <= 103 """

import sys
sys.setrecursionlimit(10**9)

class Solution:
    def findCatalan(self, n : int) -> int:
        # code here
        # !2n/((!n+1)(!n))
        def factorial(n):
            return 1 if n==1 else n*factorial(n-1)
        Mod=10**9+7
        a=factorial(2*n)%Mod
        b=factorial(n)%Mod
        c=factorial(n+1)%Mod
        return (a * (pow(b * c, Mod - 2, Mod))) % Mod



#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.findCatalan(n)
        
        print(res)
        

# } Driver Code Ends