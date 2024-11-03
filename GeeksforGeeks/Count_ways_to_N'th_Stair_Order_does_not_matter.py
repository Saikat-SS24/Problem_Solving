""" There are n stairs, and a person standing at the bottom wants to reach the top. The person can climb either 
1 stair or 2 stairs at a time. Count the number of ways, the person can reach the top (order does not matter).
Note: Order does not matter means for n = 4:- {1 2 1},{2 1 1},{1 1 2} are considered same.

Examples :

Input: n = 4
Output: 3
Explanation: Three ways to reach at 4th stair. They are {1, 1, 1, 1}, {1, 1, 2}, {2, 2}.

Input: n = 5
Output: 3
Explanation: Three ways to reach at 5th stair. They are {1, 1, 1, 1, 1}, {1, 1, 2, 1} and {1, 2, 2}.

Expected Time Complexity: O(n)
Expected Space Complexity: O(n)

Constraints:
1 ≤ n ≤ 104 """

#User function Template for python3

class Solution:
	def nthStair(self,n):
		# Code here
        res = int(n/2 + 1)
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.nthStair(n)
		print(ans)

# } Driver Code Ends