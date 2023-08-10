""" Given a sorted array A[] of size N, delete all the duplicated elements from A[]. Modify the array such that 
if there are X distinct elements in it then the first X positions of the array should be filled with them in 
increasing order and return the number of distinct elements in the array.

Note:
1. Don't use set or HashMap to solve the problem.
2. You must return the number of distinct elements(X) in the array, the driver code will print all the 
elements of the modified array from index 0 to X-1 as output of your code.

Example 1:

Input:
N = 5
Array = {2, 2, 2, 2, 2}
Output: 2
Explanation: After removing all the duplicates only one instance of 2 will remain i.e. {2} so modify 
array will contains 2 at first position and you should return 1 after modify the array.

Example 2:

Input:
N = 4
Array = {1, 2, 2, 4}
Output: 1 2 4
Explation: After removing all duplicates modify array will contains {1, 2, 4} at first 3 positions 
so you should return 3 after modify the array. """

#User function template for Python

class Solution:	
	def remove_duplicate(self, A, N):
		# code here
		i = 0
		for j in range(1,N):
		    if(A[i] != A[j]):
		        i+=1
		        A[i]=A[j]
		return i+1


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        N = int(input())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        n = ob.remove_duplicate(A,N)
        for i in range(n):
            print(A[i], end=" ")
        print()


# } Driver Code Ends