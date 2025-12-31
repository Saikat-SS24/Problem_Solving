## Kth smallest element in a Matrix

Given a matrix mat[][] of size n*n, where each row and column is sorted in non-decreasing order. Find the kth 
smallest element in the matrix.

## Examples

Input: n = 4, mat[][] = [[16, 28, 60, 64], [22, 41, 63, 91], [27, 50, 87, 93], [36, 78, 87, 94]], k = 3

Output: 27

Explanation: 27 is the 3rd smallest element.

Input: n = 4, mat[][] = [[10, 20, 30, 40], [15, 25, 35, 45], [24, 29, 37, 48], [32, 33, 39, 50]], k = 7

Output: 30

Explanation: 30 is the 7th smallest element.

### Constraints
- 1 <= n <= 500
- 1 <= mat[i][j] <= 10000
- 1 <= k <= n*n 

## Solution

```bash
class Solution:
    def kthSmallest(self, matrix, k):
        # code here
        n = len(matrix)
        arr = []
        for i in range(n):
            for j in range(n):
                arr.append(matrix[i][j])
                
        arr.sort()
        return arr[k-1]
```