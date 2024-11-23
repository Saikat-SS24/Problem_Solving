""" Given a positive integer k and an array arr[] denoting heights of towers, you have to modify the height of each 
tower either by increasing or decreasing them by k only once.
Find out what could be the possible minimum difference of the height of shortest and longest towers after you have 
modified each tower.

Note: A slight modification of the problem can be found here. 

Examples:

Input: k = 2, arr[] = [1, 5, 8, 10]
Output: 5
Explanation: The array can be modified as [3, 3, 6, 8]. The difference between the largest and the smallest is 
8 - 3 = 5.

Input: k = 3, arr[] = [3, 9, 12, 16, 20]
Output: 11
Explanation: The array can be modified as [6, 12, 9, 13, 17]. The difference between the largest and the smallest is 
17 - 6 = 11. 

Constraints
1 ≤ k ≤ 104
1 ≤ number of towers ≤ 105
0 ≤ arr[i] ≤ 105  """

#User function Template for python3

class Solution:
    def getMinDiff(self,k, arr):
        # code here
        n = len(arr)
        arr.sort()
        # If we increase all heights by k or decrease all
        # heights by k, the result will be arr[n - 1] - arr[0]
        res = arr[n - 1] - arr[0]
        # For all indices i, increment arr[0...i-1] by k and
        # decrement arr[i...n-1] by k
        for i in range(n):
            # Minimum height after modification
            minH = min(arr[0] + k, arr[i] - k)
            # Maximum height after modification
            maxH = max(arr[i - 1] + k, arr[n - 1] - k)
            # Store the minimum difference as result
            res = min(res, maxH - minH)
        
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        arr = list(map(int, input().strip().split()))
        solution = Solution()
        res = solution.getMinDiff(k, arr)
        print(res)
        print("~")
# } Driver Code Ends