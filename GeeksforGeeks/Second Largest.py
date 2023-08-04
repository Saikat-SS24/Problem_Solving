""" Given an array Arr of size N, print second largest distinct element from an array.

Input: 
N = 6
Arr[] = {12, 35, 1, 10, 34, 1}
Output: 34
Explanation: The largest element of the 
array is 35 and the second largest element
is 34.

Input: 
N = 3
Arr[] = {10, 5, 10}
Output: 5
Explanation: The largest element of 
the array is 10 and the second 
largest element is 5. """


#User function Template for python3
class Solution:

	def print2largest(self,arr, n):
	    arr.sort()
	    second_largest=-1
	    
	    for i in range(n-2, -1, -1):
	        if arr[i] != arr[n-1]:
	            second_largest=arr[i]
	            break
	   
	    return second_largest

#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends