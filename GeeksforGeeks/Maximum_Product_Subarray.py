""" Given an array arr[] that contains positive and negative integers (may contain 0 as well). Find the maximum product 
that we can get in a subarray of arr.

Note: It is guaranteed that the output fits in a 32-bit integer.

Examples

Input: arr[] = [-2, 6, -3, -10, 0, 2]
Output: 180
Explanation: The subarray with maximum product is {6, -3, -10} with product = 6 * (-3) * (-10) = 180.

Input: arr[] = [-1, -3, -10, 0, 60]
Output: 60
Explanation: The subarray with maximum product is {60}.

Input: arr[] = [2, 3, 4] 
Output: 24 
Explanation: For an array with all positive elements, the result is product of all elements. 

Constraints:
1 ≤ arr.size() ≤ 106
-10  ≤  arr[i]  ≤  10

ApproaWe will follow a simple approach that is to traverse from the start and keep track of the running product 
and if the running product is greater than the max product, then we update the max product. Also, 
if we encounter ‘0’ then make product of all elements till now equal to 1 because from the next element, we will start 
a new subarray.
Problem will occur when our array will contain odd no. of negative elements. In that case, we have to reject one 
negative element so that we can even no. of negative elements and their product can be positive. Now, since subarray 
should be contiguous so we can’t simply reject any one negative element. We have to either reject the first negative 
element or the last negative element.
Now, if we traverse from start then only the last negative element can be rejected and if we traverse from the last 
then the first negative element can be rejected. So we will traverse from both ends and find the maximum product 
subarray.ch - Traversing in both directions – O(n) Time and O(1) Space """

#User function Template for python3

class Solution:

    # Function to find maximum
    # product subarray
    def maxProduct(self,arr):
        # code here
        n = len(arr)
        maxProd = float('-inf')
        # leftToRight to store product from left to Right
        leftToRight = 1
        # rightToLeft to store product from right to left
        rightToLeft = 1
      
        for i in range(n):
            if leftToRight == 0:
                leftToRight = 1
            if rightToLeft == 0:
                rightToLeft = 1
          
            # calculate product from index left to right
            leftToRight *= arr[i]
          
            # calculate product from index right to left
            j = n - i - 1
            rightToLeft *= arr[j]
            maxProd = max(leftToRight, rightToLeft, maxProd)
        
        return maxProd

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends