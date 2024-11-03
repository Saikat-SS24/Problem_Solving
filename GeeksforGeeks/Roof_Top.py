""" You are given the heights of consecutive buildings. You can move from the roof of a building to the roof of the 
next adjacent building. You need to find the maximum number of consecutive steps you can put forward such that you 
gain an increase in altitude with each step.

Examples:

Input: arr[] = [1, 2, 2, 3, 2]
Output: 1
Explanation: 1, 2, or 2, 3 are the only consecutive buildings with increasing heights thus maximum number of 
consecutive steps with an increase in gain in altitude would be 1 in both cases.

Input: arr[] = [1, 2, 3, 4]
Output: 3
Explanation: 1 to 2 to 3 to 4 is the jump of length 3 to have a maximum number of buildings with increasing heights, 
so maximum steps with increasing altitude becomes 3.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 <= arr.size() <= 106
1 <= arr[i] <= 105  """

#User function Template for python3

class Solution:
    
    #Function to find maximum number of consecutive steps 
    #to gain an increase in altitude with each step.
    def maxStep(self, arr):
        #Your code here
        max_steps = 0
        current_steps = 0
        # Traverse through the array of building heights
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                current_steps += 1
                max_steps = max(max_steps, current_steps)
            else:
                current_steps = 0  # Reset the count if the height doesn't increase
        
        return max_steps

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.maxStep(arr))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends