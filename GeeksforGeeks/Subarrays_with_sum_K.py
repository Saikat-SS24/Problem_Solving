""" Given an unsorted array of integers, find the number of continuous subarrays having sum exactly equal to a given 
number k.

Examples:

Input: arr = [10, 2, -2, -20, 10], k = -10
Output: 3
Explaination: Subarrays: arr[0...3], arr[1...4], arr[3...4] have sum exactly equal to -10.

Input: arr = [9, 4, 20, 3, 10, 5], k = 33
Output: 2
Explaination: Subarrays: arr[0...2], arr[2...4] have sum exactly equal to 33.

Input: arr = [1, 3, 5], k = 0
Output: 0
Explaination: No subarray with 0 sum.

Constraints:
1 ≤ arr.size() ≤ 105
-103 ≤ arr[i] ≤ 103
-107 ≤ k ≤ 107

Approach : The idea is to use a Hash Map to store the count of every prefix sum of the array. For each index i, 
with a current prefix sum currSum, we check if (currSum – k) exists in the map. If it does, it indicates the presence 
of a subarray ending at i with the given sum k. In such cases, we increment the result with the count of (currSum – k) 
stored in hash map. """

#User function Template for python3

class Solution:
    def countSubarrays(self, arr, k):
        # code here
        prefixSums = {}
        res = 0
        currSum = 0
        for val in arr:
            # Add current element to sum so far
            currSum += val
            # If currSum is equal to desired sum, then a new subarray is found
            if currSum == k:
                res += 1
            # Check if the difference exists in the prefixSums dictionary
            if currSum - k in prefixSums:
                res += prefixSums[currSum - k]
            # Add currSum to the dictionary of prefix sums
            prefixSums[currSum] = prefixSums.get(currSum, 0) + 1
    
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        k = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        res = ob.countSubarrays(arr, k)
        print(res)
        print("~")

# } Driver Code Ends