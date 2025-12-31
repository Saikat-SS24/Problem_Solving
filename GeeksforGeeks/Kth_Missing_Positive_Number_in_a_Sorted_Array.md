## Kth Missing Positive Number in a Sorted Array

Given a sorted array of distinct positive integers arr[], we need to find the kth positive number that is missing 
from arr[].  

## Examples 

Input: arr[] = [2, 3, 4, 7, 11], k = 5

Output: 9

Explanation: Missing are 1, 5, 6, 8, 9, 10… and 5th missing number is 9.

Input: arr[] = [1, 2, 3], k = 2

Output: 5

Explanation: Missing are 4, 5, 6… and 2nd missing number is 5.

Input: arr[] = [3, 5, 9, 10, 11, 12], k = 2

Output: 2

Explanation: Missing are 1, 2, 4, 6… and 2nd missing number is 2.

Constraints:
- 1 <= arr.size() <= 105
- 1 <= k <= 105
- 1 <= arr[i]<= 106 """

## Solution

```bash
#User function Template for python3
class Solution:
    def kthMissing(self, arr, k):
        # code here
        n = len(arr)
        for i in range(n):
            if arr[i] > (k + i):
                return k + i
                
        return k + n

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.kthMissing(A, D)
        print(ans)
        print("~")
# } Driver Code Ends
```