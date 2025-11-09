## Frog Jump
Given an integer array height[] where height[i] represents the height of the i-th stair, a frog starts from the
first stair and wants to reach the last stair. From any stair i, the frog has two options: it can either jump to the 
(i+1)th stair or the (i+2)th stair. The cost of a jump is the absolute difference in height between the two stairs. 
Determine the minimum total cost required for the frog to reach the last stair.

Example:

Input: heights[] = [20, 30, 40, 20]

Output: 20

Explanation:  Minimum cost is incurred when the frog jumps from stair 0 to 1 then 1 to 3:
jump from stair 0 to 1: cost = |30 - 20| = 10
jump from stair 1 to 3: cost = |20 - 30| = 10
Total Cost = 10 + 10 = 20

Input: heights[] = [30, 20, 50, 10, 40]

Output: 30

Explanation: Minimum cost will be incurred when frog jumps from stair 0 to 2 then 2 to 4:
jump from stair 0 to 2: cost = |50 - 30| = 20
jump from stair 2 to 4: cost = |40 - 50| = 10
Total Cost = 20 + 10 = 30

Constraints:

1 ≤ height.size() ≤ 105

0 ≤ height[i] ≤ 104  

```bash
class Solution:
    def minCost(self, height):
        # code here
        n = len(height)
        if n == 1:
            return 0
        # Variables prev1 and prev2 to store the result
        # of last and second last states
        prev2 = 0
        prev1 = abs(height[1] - height[0])
        
        for i in range(2, n):
            curr = min(prev1 + abs(height[i] - height[i - 1]),
                       prev2 + abs(height[i] - height[i - 2]))
            # Updating prev2 to previous result and 
            # prev1 to current result
            prev2 = prev1
            prev1 = curr
        # In the last iteration, final value 
        # of curr is stored in  prev1
        return prev1
```