""" Given an array Arr of size N containing positive integers. Find the maximum sum of a any possible subsequence such 
that no two numbers in the subsequence should be adjacent in Arr.

Example 1:

Input:
N = 6
Arr[] = {5, 5, 10, 100, 10, 5}
Output: 110
Explanation: If you take indices 0, 3
and 5, then Arr[0]+Arr[3]+Arr[5] =
5+100+5 = 110.
Example 2:

Input:
N = 4
Arr[] = {3, 2, 7, 10}
Output: 13
Explanation: 3 and 10 forms a non
continuous subsequence with maximum
sum.
Your Task:
You don't need to read input or print anything. Your task is to complete the function findMaxSum() which takes the 
array of integers Arr and N as parameters and returns an the maximum sum possible of any valid subsequence.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 105
1 ≤ Arri ≤ 105 """


#User function Template for python3
class Solution:
	
	def findMaxSum(self,arr, n):
		# code here
        res = 0
		pre = 0
		cur = 0
		for i in range(n):
		    cur = pre+arr[i]
		    pre = res
		    res = max(cur,res)
		return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaxSum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends