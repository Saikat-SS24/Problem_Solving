""" Given an array arr[] and an integer k where k is smaller than the size of the array, the task is to find the 
kth smallest element in the given array. It is given that all array elements are distinct.

Follow up: Don't solve it using the inbuilt sort function.

Examples :

Input: arr[] = [7, 10, 4, 3, 20, 15], k = 3
Output:  7
Explanation: 3rd smallest element in the given array is 7.

Input: arr[] = [7, 10, 4, 20, 15], k = 4 
Output:  15
Explanation: 4th smallest element in the given array is 15.

Expected Time Complexity: O(n+(max_element) )
Expected Auxiliary Space: O(max_element)
Constraints:
1 <= arr.size <= 106
1<= arr[i] <= 106
1 <= k <= n  """

#User function Template for python3


class Solution:

    def kthSmallest(self, arr,k):
        # First, find the maximum element in the array
        max_element = max(arr)

        # Create a dictionary to store the frequency of each 
        # element in the input array
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
    
        # Keep track of the cumulative frequency of elements 
        # in the input array
        count = 0
        for i in range(max_element + 1):
            if i in freq:
                count += freq[i]
                if count >= k:
                    # If we have seen k or more elements, 
                    # return the current element
                    return i
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    import random
    t = int(input())
    for tcs in range(t):
        # n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.kthSmallest(arr, k))

# } Driver Code Ends