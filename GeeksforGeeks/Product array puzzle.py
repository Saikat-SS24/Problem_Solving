""" Given an array nums[], construct a Product Array nums[] such that nums[i] is equal to the product of all the 
elements of nums except nums[i].

Examples:

Input: nums[] = [10, 3, 5, 6, 2]
Output: [180, 600, 360, 300, 900]
Explanation: For i=0, P[i] = 3*5*6*2 = 180.
For i=1, P[i] = 10*5*6*2 = 600.
For i=2, P[i] = 10*3*6*2 = 360.
For i=3, P[i] = 10*3*5*2 = 300.
For i=4, P[i] = 10*3*5*6 = 900.

Input: nums[] = [12,0]
Output: [0, 12]

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Constraints:
1 <= nums.size() <= 1000
0 <= nums[i] <= 200
nums[i] may contain duplicates.  """

#User function Template for python3

class Solution:
    def productExceptSelf(self, nums):
        #code here
        n = len(nums)
        # Create empty arrays for left, right and the product
        left = [1] * n
        right = [1] * n
        product = [1] * n
        
        # Fill the left array
        for i in range(1, n):
            left[i] = nums[i-1] * left[i-1]
        
        # Fill the right array
        for i in range(n-2, -1, -1):
            right[i] = nums[i+1] * right[i+1]
        
        # Fill the product array by multiplying left and right arrays
        for i in range(n):
            product[i] = left[i] * right[i]
        
        return product

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]

        ans = Solution().productExceptSelf(arr)
        print(*ans)

# } Driver Code Ends