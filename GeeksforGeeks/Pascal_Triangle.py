""" Given a positive integer N, return the Nth row of pascal's triangle.
Pascal's triangle is a triangular array of the binomial coefficients formed by summing up the elements of previous row.
The elements can be large so return it modulo 109 + 7.

Example 1:

Input:
N = 4
Output: 
1 3 3 1
Explanation: 
4th row of pascal's triangle is 1 3 3 1.

Example 2:

Input:
N = 5
Output: 
1 4 6 4 1
Explanation: 
5th row of pascal's triangle is 1 4 6 4 1.
Your Task:
Complete the function nthRowOfPascalTriangle() which takes n, as input parameters and returns an array representing the
answer. You don't to print answer or take inputs.

Expected Time Complexity: O(N2)
Expected Auxiliary Space: O(N2)

Constraints:
1 ≤ N ≤ 103 """

#User function Template for python3

#User function Template for python3
class Solution:

	def nthRowOfPascalTriangle(self,n):
	    # code here
	    mod=10**9+7
	    if n==1:
	        return [1]
	    else:
	        prev=[1]
	        for i in range(1,n):
	            curr=[1]
	            for j in range(i-1):
	                curr.append((prev[j+1]+prev[j])%mod)
	            curr.append(1)
	            prev=curr
	        return curr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

	tc=int(input())
	while tc > 0:
	    n=int(input())
	    ob = Solution()
	    ans=ob.nthRowOfPascalTriangle(n)
	    for x in ans:
	        print(x, end=" ")
	    print()
	    tc=tc-1
# } Driver Code Ends