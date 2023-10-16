""" You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1. A group of connected 
1s forms an island. Two 1s are connected if they share one of their sides with each other.

Return the size of the largest island in the grid after applying this operation.

Example 1:

Input: 
grid = [[1,0],[0,1]]
Output:
3
Explanation:
Change any one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:

Input: 
grid = [[1,1],[1,0]]
Output:
4
Explanation:
Change the only 0 to 1 and make the island bigger, then we get an island with area = 4.
Example 3:

Input: 
grid = [[1,1],[1,1]]
Output:
4
Explanation:
Can't change any 0 to 1, only one island possible with area = 4.
Your Task:

You don't have to read input or print anything. You have to complete the functions largestIsland(), which takes binary
matrix as input and returns an integer denoting the size of the largest island in grid after applying the operation.

Constraints:

1 <= n <= 500
0 <= grid[i][j] <= 1 (grid[i][j] ∈ {0, 1} and 0<=i,j<n)  """


from typing import List

class Solution:
    def largestIsland(self, grid : List[List[int]]) -> int:
        # Code here
        n = len(grid)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        parentSize = {}

        def is_valid(i, j):
            return 0 <= i < n and 0 <= j < n

        def set_graph_parent(graphParent, grid, i, j, parent):
            graphParent[i][j] = parent
            count = 1
            for dir in directions:
                dx, dy = i + dir[0], j + dir[1]
                if is_valid(dx, dy) and grid[dx][dy] == 1 and graphParent[dx][dy] == -1:
                    count += set_graph_parent(graphParent, grid, dx, dy, parent)
            parentSize[parent] = count
            return count

        graphParent = [[-1] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and graphParent[i][j] == -1:
                    set_graph_parent(graphParent, grid, i, j, i * n + j)

        ans = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    distinct_parent = set()
                    for dir in directions:
                        dx, dy = i + dir[0], j + dir[1]
                        if is_valid(dx, dy) and grid[dx][dy] == 1 and graphParent[dx][dy] not in distinct_parent:
                            distinct_parent.add(graphParent[dx][dy])
                    temp = 0
                    for parent in distinct_parent:
                        temp += parentSize[parent]
                    ans = max(ans, temp + 1)
                else:
                    ans = max(ans, parentSize[graphParent[i][j]])

        return ans






#{ 
 # Driver Code Starts

class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        grid=IntMatrix().Input(n,n)
        
        obj = Solution()
        res = obj.largestIsland(grid)
        
        print(res)
# } Driver Code Ends