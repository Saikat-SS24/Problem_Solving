""" Given an array arr containing the lengths of the different ropes, we need to connect these ropes to form one rope. 
The cost to connect two ropes is equal to sum of their lengths. The task is to connect the ropes with minimum cost.  

Examples:

Input: arr[] = [4, 3, 2, 6]
Output: 29
Explanation: We can connect the ropes in following ways.
1) First connect ropes of lengths 2 and 3. Which makes the array [4, 5, 6]. Cost of this operation 2 + 3 = 5. 
2) Now connect ropes of lengths 4 and 5. Which makes the array [9, 6]. Cost of this operation 4 + 5 = 9.
3) Finally connect the two ropes and all ropes have connected. Cost of this operation 9 + 6 =15
Total cost for connecting all ropes is 5 + 9 + 15 = 29. This is the optimized cost for connecting ropes. 
Other ways of connecting ropes would always have same or more cost. For example, if we connect 4 and 6 first 
(we get three rope of 3, 2 and 10), then connect 10 and 3 (we gettwo rope of 13 and 2). Finally we connect 13 and 2. 
Total cost in this way is 10 + 13 + 15 = 38.

Input: arr[] = [4, 2, 7, 6, 9]
Output: 62 
Explanation: First, connect ropes 4 and 2, which makes the array [6, 7, 6, 9]. Cost of this operation 4 + 2 = 6. 
Next, add ropes 6 and 6, which results in [12, 7, 9]. Cost of this operation 6 + 6 = 12.
Then, add 7 and 9, which makes the array [12,16]. Cost of this operation 7 + 9 = 16. And
finally, add these two which gives [28]. Hence, the total cost is 6 + 12 + 16 + 28 = 62.

Expected Time Complexity: O(n logn)
Expected Auxilliary Space: O(n) 

Constraints:
1 ≤ arr.size() ≤ 205
1 ≤ arr[i] ≤ 106  """

#User function Template for python3
import heapq

class Solution:
    #Function to return the minimum cost of connecting the ropes.
   def minCost(self, arr):
        # code here
        # Create a priority queue out of the
        # given list
        heapq.heapify(arr)
    
        # Initialize result
        res = 0
    
        # While size of priority queue
        # is more than 1
        while(len(arr) > 1):
    
            # Extract shortest two ropes from arr
            first = heapq.heappop(arr)
            second = heapq.heappop(arr)
    
            # Connect the ropes: update result
            # and insert the new rope to arr
            res += first + second
            heapq.heappush(arr, first + second)
    
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
import heapq
from collections import defaultdict
# Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        a = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.minCost(a))

# } Driver Code Ends