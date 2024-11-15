""" Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are 
non-decreasing.

Return the length of the shortest subarray to remove.

A subarray is a contiguous subsequence of the array.

Example 1:
Input: arr = [1,2,3,10,4,2,3,5]
Output: 3
Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The remaining elements after that will be 
[1,2,3,3,5] which are sorted.
Another correct solution is to remove the subarray [3,10,4].

Example 2:
Input: arr = [5,4,3,2,1]
Output: 4
Explanation: Since the array is strictly decreasing, we can only keep a single element. Therefore we need to remove a 
subarray of length 4, either [5,4,3,2] or [4,3,2,1].

Example 3:
Input: arr = [1,2,3]
Output: 0
Explanation: The array is already non-decreasing. We do not need to remove any elements.
 
Constraints:
1 <= arr.length <= 105
0 <= arr[i] <= 109  """

class Solution:
  def findLengthOfShortestSubarray(self, arr: list[int]) -> int:
    n = len(arr)
    l = 0
    r = n - 1

    # arr[0..l] is non-decreasing.
    while l < n - 1 and arr[l + 1] >= arr[l]:
      l += 1
    # arr[r..n - 1] is non-decreasing.
    while r > 0 and arr[r - 1] <= arr[r]:
      r -= 1
    # Remove arr[l + 1..n - 1] or arr[0..r - 1].
    ans = min(n - 1 - l, r)

    # Since arr[0..l] and arr[r..n - 1] are non-decreasing, we place pointers
    # at the rightmost indices, l and n - 1, and greedily shrink them toward
    # the leftmost indices, 0 and r, respectively. By removing arr[i + 1..j],
    # we ensure that `arr` becomes non-decreasing.
    i = l
    j = n - 1
    while i >= 0 and j >= r and j > i:
      if arr[i] <= arr[j]:
        j -= 1
      else:
        i -= 1
      ans = min(ans, j - i)

    return ans