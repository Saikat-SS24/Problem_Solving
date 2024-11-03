"""Given an incomplete Sudoku configuration in terms of a 9 x 9  2-D square matrix (grid[][]), the task is to find
a solved Sudoku. For simplicity, you may assume that there will be only one unique solution.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Zeros in the grid indicates blanks, which are to be filled with some number between 1-9. You can not replace 
the element in the cell which is not blank.


Sample Sudoku for you to get the logic for its solution:

|3| |6|5| |8|4| | |
|5|2| | | | | | | |
| |8|7| | | | |3|1|
| | |3| |1| | |8| |
|9| | |8|6|3| | |5|
| |5| | |9| |6| | |
|1|3| | | | |2|5| |
| | | | | | | |7|4|
| | |5|2| |6|3| | |


Example 1:

Input:
grid[][] = 
[[3 0 6 5 0 8 4 0 0],
[5 2 0 0 0 0 0 0 0],
[0 8 7 0 0 0 0 3 1 ],
[0 0 3 0 1 0 0 8 0],
[9 0 0 8 6 3 0 0 5],
[0 5 0 0 9 0 6 0 0],
[1 3 0 0 0 0 2 5 0],
[0 0 0 0 0 0 0 7 4],
[0 0 5 2 0 6 3 0 0]]
Output:
True
3 1 6 5 7 8 4 9 2
5 2 9 1 3 4 7 6 8
4 8 7 6 2 9 5 3 1
2 6 3 4 1 5 9 8 7
9 7 4 8 6 3 1 2 5
8 5 1 7 9 2 6 4 3
1 3 8 9 4 7 2 5 6
6 9 2 3 5 1 8 7 4
7 4 5 2 8 6 3 1 9
Explanation: 
There exists a valid Sudoku for the input grid, which is shown in output.

Example 2:

Input:
grid[][] = 
[[3 6 6 5 0 8 4 0 0],
[5 2 0 0 0 0 0 0 0],
[0 8 7 0 0 0 0 3 1 ],
[0 0 3 0 1 0 0 8 0],
[9 0 0 8 6 3 0 0 5],
[0 5 0 0 9 0 6 0 0],
[1 3 0 0 0 0 2 5 0],
[0 0 0 0 0 0 0 7 4],
[0 0 5 2 0 6 3 0 0]]
Output:
False
Explanation: 
There does not exists a valid Sudoku for the input grid, since there are two 6s in the first row. 
Which cannot replaced."""

#User function Template for python3


class Solution:
    
    #Function to find a solved Sudoku. 
    def SolveSudoku(self,grid):
        def solve(grid, r0, c0):
            if r0 == 9:
                return True
            if c0 == 9:
                return solve(grid, r0+1, 0)
                
            if grid[r0] [c0] != 0:
                return solve(grid, r0, c0+1)
                
            for v in range(1, 10):
                if self.check(grid,r0,c0,v):
                    grid[r0] [c0] = v
                    if solve(grid, r0, c0+1):
                        return True
                    grid[r0] [c0] = 0
            return False
        return solve(grid, 0, 0)
    
    #Function to print grids of the Sudoku.    
    def printGrid(self,arr):
        
        # Your code here
        for i in range(9):
            for j in range(9):
                print(arr[i][j], end=" ")
                
                
    def check(self,arr,r0,c0,v):
        for d in range(9):
            if arr[d][c0] == v or arr[r0][d] == v:
                return False
                
        r0 = r0//3*3
        c0 = c0//3*3
        for r in range(r0, r0+3):
            for c in range(c0, c0+3):
                if grid[r][c] == v:
                    return False
        return True


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t = int(input())
    while(t>0):
        grid = [[0 for i in range(9)] for j in range(9)]
        row = [int(x) for x in input().strip().split()]
        k = 0
        for i in range(9):
            for j in range(9):
                grid[i][j] = row[k]
                k+=1
                
        ob = Solution()
            
        if(ob.SolveSudoku(grid)==True):
            ob.printGrid(grid)
            print()
        else:
            print("No solution exists")
        t = t-1
# } Driver Code Ends