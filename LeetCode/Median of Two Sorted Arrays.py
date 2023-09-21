""" Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106 """

class Solution:
  def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    n1 = len(nums1)
    n2 = len(nums2)
    if n1 > n2:
      return self.findMedianSortedArrays(nums2, nums1)

    l = 0
    r = n1

    while l <= r:
      partition1 = (l + r) // 2
      partition2 = (n1 + n2 + 1) // 2 - partition1
      maxLeft1 = -2**31 if partition1 == 0 else nums1[partition1 - 1]
      maxLeft2 = -2**31 if partition2 == 0 else nums2[partition2 - 1]
      minRight1 = 2**31 - 1 if partition1 == n1 else nums1[partition1]
      minRight2 = 2**31 - 1 if partition2 == n2 else nums2[partition2]
      if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
        return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) * 0.5 if (n1 + n2) % 2 == 0 else max(maxLeft1, maxLeft2)
      elif maxLeft1 > minRight2:
        r = partition1 - 1
      else:
        l = partition1 + 1
