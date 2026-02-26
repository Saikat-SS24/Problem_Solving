## Josephus problem

You are playing a game with n people standing in a circle, numbered from 1 to n. Starting from person 1, every kth person is eliminated in a circular fashion. The process continues until only one person remains.
Given integers n and k, return the position (1-based index) of the person who will survive.

## Examples 

#### Input: n = 5, k = 2

#### Output: 3

#### Explanation:
Firstly, the person at position 2 is killed, then the person at position 4 is killed, then the person at position 1 is killed. 

Finally, the person at position 5 is killed. So the person at position 3 survives. 

#### Input: n = 7, k = 3

#### Output: 4

#### Explanation: 
The elimination order is 3 → 6 → 2 → 7 → 5 → 1, and the person at position 4 survives.

### Constraints:
- 1 ≤ n, k ≤ 500

## Solution

```bash
class Solution:
    def josephus(self, n, k):
        # code here
        i = 1
        ans = 0
        
        # Run a while loop till i <= N
        while(i <= n):
    
            # update the value of ans
            ans = (ans + k) % i
            i += 1
        
        # returning the required answer
        return ans + 1
```