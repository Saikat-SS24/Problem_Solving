""" Given an array arr of distinct integers. Rearrange the array in such a way that the first element is the largest 
and the second element is the smallest, the third element is the second largest and the fourth element is the second 
smallest, and so on.

Examples:

Input: arr[] = [7, 1, 2, 3, 4, 5, 6]
Output: [7, 1, 6, 2, 5, 3, 4]
Explanation: The first element is first maximum and second element is first minimum and so on.

Input: arr[] = [1, 6, 9, 4, 3, 7, 8, 2]
Output: [9, 1, 8, 2, 7, 3, 6, 4]
Explanation: The first element is first maximum and second element is first minimum and so on.

Expected Time Complexity: O(nlogn).
Expected Auxiliary Space: O(n).

Constraints:
1 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 105 """

class Solution:
    def alternateSort(self,arr):
        # Your code goes here
        arr.sort()
        res = []
        left, right = 0, len(arr) - 1
        while left <= right:
            if left <= right:
                res.append(arr[right])
                right -= 1
            if left <= right:
                res.append(arr[left])
                left += 1
            
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.alternateSort(arr)
        print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends