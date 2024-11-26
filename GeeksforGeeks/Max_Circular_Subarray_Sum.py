""" Given an array of integers arr[] in a circular fashion. Find the maximum subarray sum that we can get if we assume 
the array to be circular.

Examples:

Input: arr[] = [8, -8, 9, -9, 10, -11, 12]
Output: 22
Explanation: Starting from the last element of the array, i.e, 12, and moving in a circular fashion, we have max 
subarray as 12, 8, -8, 9, -9, 10, which gives maximum sum as 22.

Input: arr[] = [10, -3, -4, 7, 6, 5, -4, -1]
Output: 23
Explanation: Maximum sum of the circular subarray is 23. The subarray is [7, 6, 5, -4, -1, 10].

Input: arr[] = [-1, 40, -14, 7, 6, 5, -4, -1] 
Output: 52
Explanation: Circular Subarray [7, 6, 5, -4, -1, -1, 40] has the maximum sum, which is 52.

Constraints:
1 <= arr.size() <= 105
-104 <= arr[i] <= 104

Approach] Using Kadane’s Algorithm – O(n) Time and O(1) Space
This approach is similar to the previous one, but the key difference is that we’re using Kadane’s algorithm to find 
the circular subarray sum as well. The maximum sum of a circular subarray can be defined as the total sum of the array 
minus the sum of a subarray in the middle. So, to maximize the circular subarray sum, we need to minimize the subarray 
sum. 
Maximum-circular-subarray-sum
Maximum Circular Subarray Sum = Total Sum – Minimum Subarray Sum.
If the minimum subarray sum equals the total sum of the array, we return the normal maximum subarray sum, because if 
all elements are negative, the circular sum would be zero, but the answer will be negative only. """

#User function Template for python3

#Complete this function
#Function to find maximum circular subarray sum.
def circularSubarraySum(arr):
    ##Your code here
    totalSum = 0    
    currMaxSum = 0
    currMinSum = 0
    maxSum = arr[0]
    minSum = arr[0]
    
    for i in range(len(arr)):
      
        # Kadane's to find maximum sum subarray
        currMaxSum = max(currMaxSum + arr[i], arr[i])
        maxSum = max(maxSum, currMaxSum) 
        
        # Kadane's to find minimum sum subarray
        currMinSum = min(currMinSum + arr[i], arr[i])
        minSum = min(minSum, currMinSum)
        
        # Sum of all the elements of input array
        totalSum += arr[i]
    
    normalSum = maxSum
    circularSum = totalSum - minSum
    
    # If the minimum subarray is equal to total Sum
    # then we just need to return normalSum
    if minSum == totalSum:
        return normalSum
    
    return max(normalSum, circularSum)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
import sys

if __name__ == "__main__":
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        print(circularSubarraySum(arr))

        T -= 1
# } Driver Code Ends