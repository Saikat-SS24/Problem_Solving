""" Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 
3.

Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
 
Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1. """


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        # initialize max
        result = 0
        for i in range(0,len(nums)):
            # Reset count when 0 is found
            if (nums[i] == 0):
                count = 0
 
            # If 1 is found, increment count
            # and update result if count 
            # becomes more.
            else:
             
                # increase count
                count += 1
                result = max(result, count) 
         
        return result