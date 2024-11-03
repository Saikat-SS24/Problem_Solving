""" Given an array arr[] of n positive integers. Push all the zeros of the given array to the right end of the array 
while maintaining the order of non-zero elements. Do the mentioned change in the array in-place.

Example 1:

Input:
N = 5
Arr[] = {3, 5, 0, 0, 4}
Output: 3 5 4 0 0
Explanation: The non-zero elements
preserve their order while the 0
elements are moved to the right.

Example 2:

Input:
N = 4
Arr[] = {0, 0, 0, 4}
Output: 4 0 0 0
Explanation: 4 is the only non-zero
element and it gets moved to the left.
Your Task:
You don't need to read input or print anything. Complete the function pushZerosToEnd() which takes the array arr[] and
its size n as input parameters and modifies arr[] in-place such that all the zeroes are moved to the right.  

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 105
0 ≤ arri ≤ 105 """

#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr, n):
    	# code here
        count = 0
        for i in range(n):
            if arr[i] != 0: 
                # here count is incremented 
                arr[count] = arr[i] 
                count += 1
      
        # Now all non-zero elements have been 
        # shifted to front and 'count' is set 
        # as index of first 0. Make all  
        # elements 0 from count to end. 
        while count < n: 
            arr[count] = 0
            count += 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends