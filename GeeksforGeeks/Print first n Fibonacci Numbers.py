""" Given a number N, find the first N Fibonacci numbers. The first two number of the series are 1 and 1.

Example 1:

Input:
N = 5
Output: 1 1 2 3 5
Example 2:

Input:
N = 7
Output: 1 1 2 3 5 8 13
Your Task:
Your task is to complete printFibb() which takes single argument N and returns a list of first N Fibonacci numbers.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).
Note: This space is used to store and return the answer for printing purpose.

Constraints:
1<= N <=84 """


#User function Template for python3

class Solution:
    #Function to return list containing first n fibonacci numbers.
    def printFibb(self,n):
        # your code here
        ans=[1,1]
        for i in range(3,n+1):
            ans.append(ans[-1]+ans[-2])
        return ans if n>1 else [1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        
        n=int(input())
        res = Solution().printFibb(n)
        for i in range (len(res)):
            print (res[i], end = " ") 
        print()
# } Driver Code Ends