""" Given a boolean matrix of size RxC where each cell contains either 0 or 1, modify it such that if a matrix cell 
matrix[i][j] is 1 then all the cells in its ith row and jth column will become 1.

Example 1:

Input:
R = 2, C = 2
matrix[][] = {{1, 0},
              {0, 0}}
Output: 
1 1
1 0 
Explanation:
Only cell that has 1 is at (0,0) so all 
cells in row 0 are modified to 1 and all 
cells in column 0 are modified to 1.

Example 2:

Input:
R = 4, C = 3
matrix[][] = {{ 1, 0, 0},
              { 1, 0, 0},
              { 1, 0, 0},
              { 0, 0, 0}}
Output: 
1 1 1
1 1 1
1 1 1
1 0 0 
Explanation:
The position of cells that have 1 in
the original matrix are (0,0), (1,0)
and (2,0). Therefore, all cells in row
0,1,2 are and column 0 are modified to 1. 
Your Task:
You dont need to read input or print anything. Complete the function booleanMatrix() that takes the matrix as input parameter and modifies it in-place.

Expected Time Complexity: O(R * C)
Expected Auxiliary Space: O(R + C) 

Constraints:
1 ≤ R, C ≤ 1000
0 ≤ matrix[i][j] ≤ 1 """

#User function Template for python3

from copy import deepcopy
#Function to modify the matrix such that if a matrix cell matrix[i][j]
#is 1 then all the cells in its ith row and jth column will become 1.
def booleanMatrix(matrix):
    # code here 
    # Create a deep copy of the input matrix
    mat = deepcopy(matrix)
    rows, cols = len(matrix), len(matrix[0])
    
    # Lists to keep track of rows and columns to be modified

    rows_to_modify = [False] * rows
    cols_to_modify = [False] * cols
    
    # Traverse the matrix and mark rows and columns to be modified

    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 1:
                rows_to_modify[i] = True
                cols_to_modify[j] = True
    
    # Modify the matrix based on the marked rows and columns

    for i in range(rows):
        for j in range(cols):
            if rows_to_modify[i] or cols_to_modify[j]:
                matrix[i][j] = 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        matrix = []
        for i in range(r):
            line = [int(x) for x in input().strip().split()]
            matrix.append(line)
        booleanMatrix(matrix)
        for i in range(r):
            for j in range(c):
                print(matrix[i][j], end=' ')
            print()


# } Driver Code Ends