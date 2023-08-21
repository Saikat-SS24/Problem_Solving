""" Given a matrix of order nxm, composed of only 0's and 1's, find the number of 1's in the matrix that are surrounded by an even number (>0) of 0's. The surrounding of a cell in the matrix is defined as the elements above, below, on left, on right as well as the 4 diagonal elements around the cell of the matrix. Hence, the surrounding of any matrix elements is composed of 8 elements. Find the number of such 1's.

Example 1:

Input: 
matrix = {{1, 0, 0}, 
          {1, 1, 0}, 
          {0, 1, 0}}
Output: 
1
Explanation: 
1 that occurs in the 1st row and 1st column, has 3 surrounding elements 0,1 and 1. The occurrence of zero is odd. 
1 that occurs in 2nd row and 1st column has 5 surrounding elements 1,0,1,1 and 0. The occurrence of zero is even. 
1 that occurs in 2nd row and 2nd column has 8 surrounding elements. The occurrence of 0 is odd. 
Similarly, for the 1 that occurs in 3rd row and 2nd column, the occurrence of zero in it's 5 surrounding elements is odd. 
Hence, the output is 1.
Example 2:

Input: 
matrix = {{1}}
Output: 
0
Explanation: 
There is only 1 element in the matrix. Hence, it has no surroundings, so it's count for even 0's is 0 for the whole matrix. 
0 is even but we want occurrence of a zero in the surrounding at least once. 
Hence, output is 0.
Your Task:
You don't need to read or print anything. Your task is to complete the function Count() which takes the matrix as input parameter and returns the number of 1's which are surrounded by even number of 0's.

Expected Time Complexity: O(n * m)
Expected Space Complexity: O(1)

Constraints:
1 <= n, m <= 103 """

#User function Template for python3

class Solution:
	def Count(self, matrix):
		# Code here
		row = len(matrix)
	    col = len(matrix[0])
	    ans = 0
	    traverse = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
	    for i in range(row):
	        for j in range(col):
	            if matrix[i][j] == 1:
	                zeros=0
	                for k in traverse:
	                    new_row = i + k[0]
	                    new_col = j + k[1]
	                    if new_row>=0 and new_col>=0 and new_row < row and new_col < col:
	                        if matrix[new_row][new_col] == 0:
	                            zeros+=1
	                if zeros>0 and zeros%2 == 0:
	                    ans+=1
	    return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		matrix = []
		for _ in range(n):
			matrix.append(list(map(int,input().split())))
		ob = Solution()
		ans = ob.Count(matrix)
		print(ans)

# } Driver Code Ends