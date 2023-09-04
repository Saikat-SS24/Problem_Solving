"""Given a matrix mat of size N x M where every element is either 'O' or 'X'. Replace all 'O' with 'X' 
that are surrounded by 'X'.

A 'O' (or a set of 'O') is considered to be surrounded by 'X' if there are 'X' at locations just below, just above, 
just left and just right of it.

Example 1:

Input: 
n = 5, m = 4
mat = {{'X', 'X', 'X', 'X'}, 
       {'X', 'O', 'X', 'X'}, 
       {'X', 'O', 'O', 'X'}, 
       {'X', 'O', 'X', 'X'}, 
       {'X', 'X', 'O', 'O'}}
Output: 
ans = {{'X', 'X', 'X', 'X'}, 
       {'X', 'X', 'X', 'X'}, 
       {'X', 'X', 'X', 'X'}, 
       {'X', 'X', 'X', 'X'}, 
       {'X', 'X', 'O', 'O'}}
Explanation: 
Following the rule the above matrix is the resultant matrix. 
Example 2:

 

Input: 
n = 5, m = 4
mat = {{'X', 'O', 'X', 'X'}, 
       {'X', 'O', 'X', 'X'}, 
       {'X', 'O', 'O', 'X'}, 
       {'X', 'O', 'X', 'X'}, 
       {'X', 'X', 'O', 'O'}}
Output: 
ans = {{'X', 'O', 'X', 'X'}, 
       {'X', 'O', 'X', 'X'}, 
       {'X', 'O', 'O', 'X'}, 
       {'X', 'O', 'X', 'X'}, 
       {'X', 'X', 'O', 'O'}}
Explanation: 
Following the rule the above matrix is the resultant matrix.
Your Task:
You do not need to read input or print anything. Your task is to complete the function fill() which takes N, M and mat as input parameters ad returns a 2D array representing the resultant matrix.

Expected Time Complexity: O(n*m)
Expected Auxiliary Space: O(n*m)

Constraints:
1 ≤ n, m ≤ 500 """

#User function Template for python3

class Solution:
    def fill(self, n, m, mat):
        # code here
        if not mat:
            return mat

        # Helper function to perform DFS starting from a given cell.
        def dfs(r, c):
            if r < 0 or r >= n or c < 0 or c >= m or mat[r][c] != 'O':
                return

            mat[r][c] = 'V'  # Mark the cell as visited

            # Explore neighboring cells
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Step 1: Identify and mark all 'O' cells on the boundary as 'V'.
        for i in range(n):
            if mat[i][0] == 'O':
                dfs(i, 0)
            if mat[i][m - 1] == 'O':
                dfs(i, m - 1)
        for j in range(m):
            if mat[0][j] == 'O':
                dfs(0, j)
            if mat[n - 1][j] == 'O':
                dfs(n - 1, j)

        # Step 2: Mark any remaining unvisited 'O' cells as 'X' and restore 'V' to 'O'.
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 'O':
                    mat[i][j] = 'X'
                elif mat[i][j] == 'V':
                    mat[i][j] = 'O'

        return mat


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        mat = []
        for i in range(n):
            s = list(map(str,input().split()))
            mat.append(s)
        
        ob = Solution()
        ans = ob.fill(n, m, mat)
        for i in range(n):
            for j in range(m):
                print(ans[i][j], end = " ")
            print()
# } Driver Code Ends