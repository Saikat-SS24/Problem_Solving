""" Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero 
elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0] """

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        cnt, n = 0, len(nums)
        for i in range(n):
            if nums[i] != 0:
                nums[cnt] = nums[i]
                cnt += 1

        while(cnt < n):
            nums[cnt] = 0
            cnt += 1

        return nums