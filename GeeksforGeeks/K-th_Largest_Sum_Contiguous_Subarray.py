""" Given an array arr[] of size n, find the sum of the K-th largest sum among all contiguous subarrays. In other 
words, identify the K-th largest sum from all possible subarrays and return it.

Examples:

Input: arr[] = [3, 2, 1], k = 2 
Output: 5
Explanation: The different subarray sums we can get from the array are = [6, 5, 3, 2, 1]. Where 5 is the 2nd largest.

Input: arr[] = [2, 6, 4, 1], k = 3
Output: 11
Explanation: The different subarray sums we can get from the arrayare = [13, 12, 11, 10, 8, 6, 5, 4, 2, 1]. Where 11 
is the 3rd largest.

Constraints:
1 <= arr.size() <= 1000
1 <= k <= (n*(n+1))/2
-105 <= arr[i] <= 105  """

from typing import List


class Solution:
    def kthLargest(self, arr, k) -> int:
        # code here
        n = len(arr)
        sums = []
        for i in range(n):
            sum = 0
            for j in range(i, n):
                sum += arr[j]
                sums.append(sum)

        sums.sort(reverse=True)
    
        return sums[k - 1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import heapq

# Position this line where user code will be pasted.

#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        k = int(input())
        ob = Solution()
        res = ob.kthLargest(arr, k)
        print(res)
        print("~")
        t -= 1

# } Driver Code Ends