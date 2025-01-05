""" Given an array arr[] and an integer target. You have to find the number of pairs in the array whose sum is strictly 
less than the target.

Examples:

Input: arr[] = [7, 2, 5, 3], target = 8
Output: 2
Explanation: There are 2 pairs with sum less than 8: (2, 5) and (2, 3). 

Input: arr[] = [5, 2, 3, 2, 4, 1], target = 5
Output: 4
Explanation: There are 4 pairs whose sum is less than 5: (2, 2), (2, 1), (3, 1) and (2, 1).

Input: arr[] = [2, 1, 8, 3, 4, 7, 6, 5], target = 7
Output: 6
Explanation: There are 6 pairs whose sum is less than 7: (2, 1), (2, 3), (2, 4), (1, 3), (1, 4) and (1, 5).

Constraints:
1 <= arr.size() <= 105
0 <= arr[i] <= 104
1 <= target <= 104  """

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends
#User function Template for python3
class Solution:
    #Complete the below function
    def countPairs(self, arr, target):
        #Your code here
        arr.sort()
        left, right = 0, len(arr) - 1
        cnt = 0
        # Two pointer technique
        while left < right:
            sum = arr[left] + arr[right]
    
            # If the sum is less than target, then arr[left] 
            # will form a valid pair with every element 
            # from index left + 1 to right.
            if sum < target:
                cnt += right - left
                left += 1
            else:
                right -= 1
    
        return cnt
        

#{ 
 # Driver Code Starts.

def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        k = int(input())
        ob = Solution()
        print(ob.countPairs(A, k))
        print('~')
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends