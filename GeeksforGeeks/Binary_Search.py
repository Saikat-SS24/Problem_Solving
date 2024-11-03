""" Given a sorted array of size N and an integer K, find the position(0-based indexing) at which K is present in the 
array using binary search.

Example 1:

Input:
N = 5
arr[] = {1 2 3 4 5} 
K = 4
Output: 3
Explanation: 4 appears at index 3.

Example 2:

Input:
N = 5
arr[] = {11 22 33 44 55} 
K = 445
Output: -1
Explanation: 445 is not present.

Your Task:  
You dont need to read input or print anything. Complete the function binarysearch() which takes arr[], N and K as 
input parameters and returns the index of K in the array. If K is not present in the array, return -1.

Expected Time Complexity: O(LogN)
Expected Auxiliary Space: O(LogN) if solving recursively and O(1) otherwise. """

#Constraints:
#User function template for Python

class Solution:	
	def binarysearch(self, arr, n, k):
		# code here
		l = 0
        r = n-1
        m = int((l+r)/2)
        while l <= r:
            if arr[m] == k:
                return m
            if k<arr[m]:
                r = m-1
                m = int((l+r)/2)
            if k>arr[m]:
                l = m+1
                m = int((l+r)/2)
            if k not in arr:
                return -1


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int, input().strip().split(' ')))
        k=int(input())
        ob = Solution()
        print (ob.binarysearch(arr, n, k))


# } Driver Code Ends
1 <= N <= 105
1 <= arr[i] <= 106
1 <= K <= 106  