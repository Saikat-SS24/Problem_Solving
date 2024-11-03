""" Given an array arr[] with repeated elements, the task is to find the maximum distance between two occurrences of 
an element.

Note: You may assume that every input array has repetitions.

Examples:
Input: arr = [1, 1, 2, 2, 2, 1]
Output: 5
Explanation: distance for 1 is: 5-0 = 5, distance for 2 is : 4-2 = 2, So max distance is 5.

Input: arr = [3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]
Output: 10
Explanation: maximum distance for 2 is 11-1 = 10, maximum distance for 1 is 4-2 = 2 ,maximum distance for 4 is 
10-5 = 5, So max distance is 10.

Expected Time Complexity :  O(n)
Expected Auxilliary Space : O(n)

Constraints:
1 <= arr.size() <= 106
1 <= arr[i] <= 109  """

class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    def maxDistance(self, arr):
        # Code here
        hist = {}
        rev_hist = {}
        n = len(arr)
        for i in range(n):
            if arr[i] not in hist:
                hist[arr[i]] = i
        for i in range(n):
            rev_hist[arr[i]] = i
            
        max_value = -1
        for k, v in hist.items():
            max_value = max(max_value, rev_hist[k] - hist[k])
        return max_value


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.maxDistance(arr))

# } Driver Code Ends