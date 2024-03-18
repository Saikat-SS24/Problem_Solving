""" Given an array A[] of N elements. The task is to return the count of the number of odd and even elements in the 
array.

Example:

Input:
N = 5
A[] = 1 2 3 4 5
Output:
3 2
Explanation:
There are 3 odd elements (1, 3, 5)
and 2 even elements (2 and 4).

Your Task:
Your task is to complete the function countOddEven() which should return the count of odd and even elements of the 
array.

Expected Time Complexity: O(N)
Expected Space Complexity: O(1)

Constraints:
1 <= N <= 106
1 <= Ai <= 106   """

#User function Template for python3

class Solution:
	def countOddEven(self, arr, n):
		#Code here
		c1,c2 = 0,0
		for i in range(n):
		    if (arr[i]%2 != 0):
		        c1 += 1
		    elif (arr[i]%2 == 0):
		        c2 += 1
		        
		return c1,c2

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    # Testcase input
    testcase = int(input())

    for _ in range(testcase):
        n = int(input())

        arr = list(map(int, input().split()))

        # Creating an object of the Solution class
        ob = Solution()

        # Calling the function to count even and odd
        res = ob.countOddEven(arr, n)

        # Printing the result
        print(*res)

# } Driver Code Ends