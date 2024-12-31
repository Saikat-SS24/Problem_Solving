""" Given an array arr[] of non-negative integers. Find the length of the longest sub-sequence such that elements in 
the subsequence are consecutive integers, the consecutive numbers can be in any order.

Examples:

Input: arr[] = [2, 6, 1, 9, 4, 5, 3]
Output: 6
Explanation: The consecutive numbers here are 1, 2, 3, 4, 5, 6. These 6 numbers form the longest consecutive 
subsquence.

Input: arr[] = [1, 9, 3, 10, 4, 20, 2]
Output: 4
Explanation: 1, 2, 3, 4 is the longest consecutive subsequence.

Input: arr[] = [15, 13, 12, 14, 11, 10, 9]
Output: 7
Explanation: The longest consecutive subsequence is 9, 10, 11, 12, 13, 14, 15, which has a length of 7.

Constraints:
1 <= arr.size() <= 105
0 <= arr[i] <= 105 """

 #User function Template for python3
 
class Solution:
    
    # arr[] : the input array
    
    #Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self,arr):
        #code here
        arr.sort()
        res = 1
        cnt = 1
        # Find the maximum length by traversing the array
        for i in range(1, len(arr)):
            # Skip duplicates
            if arr[i] == arr[i - 1]:
                continue
            # Check if the current element is equal
            # to previous element + 1
            if arr[i] == arr[i - 1] + 1:
                cnt += 1
            else:
                # Reset the count
                cnt = 1
    
            # Update the result
            res = max(res, cnt)
    
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        a = list(map(int, input().strip().split()))
        print(Solution().longestConsecutive(a))
        print("~")
# } Driver Code Ends