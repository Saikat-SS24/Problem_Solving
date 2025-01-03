""" Given a sorted array arr[] (with unique elements) and an integer k, find the index (0-based) of the largest 
element in arr[] that is less than or equal to k. This element is called the "floor" of k. If such an element does not 
exist, return -1.

Examples

Input: arr[] = [1, 2, 8, 10, 11, 12, 19], k = 0
Output: -1
Explanation: No element less than 0 is found. So output is -1.

Input: arr[] = [1, 2, 8, 10, 11, 12, 19], k = 5
Output: 1
Explanation: Largest Number less than 5 is 2 , whose index is 1.

Input: arr[] = [1, 2, 8], k = 1
Output: 0
Explanation: Largest Number less than or equal to  1 is 1 , whose index is 0.

Constraints:
1 ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤ 106
0 ≤ k ≤ arr[n-1]  """

class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,arr,k):
        #Your code here
        n = len(arr)
        for i in range(n):
            if arr[i] == k:
                return i
            if arr[i] > k:
                return i - 1
        
        return -1
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.findFloor(arr, k)
        print(ans)
        tc -= 1

# } Driver Code Ends