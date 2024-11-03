""" You are given an n x m binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.
A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the 
boundary of the grid.
Find the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

Example 1:

Input:
grid[][] = {{0, 0, 0, 0},
            {1, 0, 1, 0},
            {0, 1, 1, 0},
            {0, 0, 0, 0}}
Output:
3
Explanation:
0 0 0 0
1 0 1 0
0 1 1 0
0 0 0 0
The highlighted cells represents the land cells.
Example 2:

Input:
grid[][] = {{0, 0, 0, 1},
            {0, 1, 1, 0},
            {0, 1, 1, 0},
            {0, 0, 0, 1},
            {0, 1, 1, 0}}
Output:
4
Explanation:
0 0 0 1
0 1 1 0
0 1 1 0
0 0 0 1
0 1 1 0
The highlighted cells represents the land cells.
Your Task:

You don't need to print or input anything. Complete the function numberOfEnclaves() which takes a 2D integer matrix 
grid as the input parameter and returns an integer, denoting the number of land cells.

Expected Time Complexity: O(n * m)

Expected Space Complexity: O(n * m)

Constraints:

1 <= n, m <= 500
grid[i][j] == 0 or 1 """

#User function Template for python3

from typing import List

class Solution:    
    def numberOfEnclaves(self, grid: List[List[int]]) -> int:
        # code here
        dir = [[0, -1], [-1, 0], [1, 0], [0, 1]]
        r, c = len(grid), len(grid[0])
        border = []
        count = 0
        
        for i in range(r):
            for j in range(c):
                if grid[i][j]:
                    if i==0 or i==r-1 or j==0 or j==c-1:
                        border.append([i, j])
                    else:
                        count+=1
        
        while border:
            x, y = border.pop()
            if grid[x][y]:
                grid[x][y] = 0
                if 0<x<r-1 and 0<y<c-1:
                    count-=1
                for dx, dy in dir:
                    if -1<(x+dx)<r and -1<(y+dy)<c and grid[x+dx][y+dy]:
                        border.append([x+dx, y+dy])
        
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int,input().strip().split())
        grid = []
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])

        obj=Solution()
        print(obj.numberOfEnclaves(grid))
# } Driver Code Ends