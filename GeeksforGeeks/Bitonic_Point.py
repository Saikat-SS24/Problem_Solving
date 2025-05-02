""" Given an array of integers arr[] that is first strictly increasing and then maybe strictly decreasing, find the 
bitonic point, that is the maximum element in the array.
Bitonic Point is a point before which elements are strictly increasing and after which elements are strictly 
decreasing.

Note: It is guaranteed that the array contains exactly one bitonic point.

Examples:

Input: arr[] = [1, 2, 4, 5, 7, 8, 3]
Output: 8
Explanation: Elements before 8 are strictly increasing [1, 2, 4, 5, 7] and elements after 8 are strictly decreasing 
[3].

Input: arr[] = [10, 20, 30, 40, 50]
Output: 50
Explanation: Elements before 50 are strictly increasing [10, 20, 30 40] and there are no elements after 50.

Input: arr[] = [120, 100, 80, 20, 0]
Output: 120
Explanation: There are no elements before 120 and elements after 120 are strictly decreasing [100, 80, 20, 0].

Constraints:
3 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 106  """

#User function Template for python3
class Solution:

    def findMaximum(self, arr):
        # code here
        res = arr[0]
        for i in range(1,len(arr)):
            res = max(res, arr[i])
            
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaximum(arr)
        print(ans)
        tc -= 1
        print("~")

# } Driver Code Ends