## Sort 0s, 1s and 2s

Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order.
Note: You need to solve this problem without utilizing the built-in sort function.

## Examples

Input: arr[] = [0, 1, 2, 0, 1, 2]

Output: [0, 0, 1, 1, 2, 2]

Explanation: 0s, 1s and 2s are segregated into ascending order.

Input: arr[] = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]

Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]

Explanation: 0s, 1s and 2s are segregated into ascending order.

Follow up: Could you come up with a one-pass algorithm using only constant extra space?

### Constraints:
- 1 ≤ arr.size() ≤ 106
- 0 ≤ arr[i] ≤ 2

## Solution

```bash
class Solution:
    def sort012(self, arr):
        # code here
        c0 = 0
        c1 = 0
        c2 = 0
    
        # count 0s, 1s and 2s
        for num in arr:
            if num == 0:
                c0 += 1
            elif num == 1:
                c1 += 1
            else:
                c2 += 1
    
        idx = 0
        
        # place all the 0s
        for i in range(c0):
            arr[idx] = 0
            idx += 1
    
        # place all the 1s
        for i in range(c1):
            arr[idx] = 1
            idx += 1
    
        # place all the 2s
        for i in range(c2):
            arr[idx] = 2
            idx += 1
```