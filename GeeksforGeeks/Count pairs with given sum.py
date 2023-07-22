# Given an array of N integers, and an integer K, find the number of pairs of elements in the array whose 
# sum is equal to K.

# Input:
# N = 4, K = 6
# arr[] = {1, 5, 7, 1}
# Output: 2
# Explanation: 
# arr[0] + arr[1] = 1 + 5 = 6 
# and arr[1] + arr[3] = 5 + 1 = 6.

# Input:
# N = 4, K = 2
# arr[] = {1, 1, 1, 1}
# Output: 6
# Explanation: 
# Each 1 will produce sum 2 with any 1.
    

#User function Template for python3
import bisect
class Solution:
    def getPairsCount(self, arr, n, k):
        # code here
        arr.sort()
        x, c = 0, 0
        for i in range(n-1):
            x = k-arr[i]
 
            # Lower bound from i+1
            y = bisect.bisect_left(arr, x, i+1, n)
 
            # Upper bound from i+1
            z = bisect.bisect(arr, x, i+1, n)
            c = c+z-y
            
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends