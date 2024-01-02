""" Given an array a of length n and a number k, find the largest sum of the subarray containing at least k numbers. 
It is guaranteed that the size of array is at-least k.

Example 1:

Input : 
n = 4
a[] = {-4, -2, 1, -3}
k = 2
Output : 
-1
Explanation :
The sub-array of length at-least 2
that produces greatest sum is {-2, 1}

Example 2:

Input :
n = 6 
a[] = {1, 1, 1, 1, 1, 1}
k = 2
Output : 
6
Explanation :
The sub-array of length at-least 2
that produces greatest sum is {1, 1, 1, 1, 1, 1}
Your Task:  
You don't need to read input or print anything. Your task is to complete the function maxSumWithK() which takes the 
array a[], its size n and an integer k as inputs and returns the value of the largest sum of the subarray containing 
at least k numbers.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Constraints:
1 <= n <= 105
-105 <= a[i] <= 105
1 <= k <= n """


#User function Template for python3
from itertools import accumulate
from collections import deque

class Solution():
    def maxSumWithK(self, a, n, k):
        # Code here
        a = list(accumulate(a))
        
        maxs = deque()
        r = float('-inf')
        for i in range(n-1, -1, -1):
            if a[i] > r:
                r = max(a[i], r)
                maxs.appendleft((r, i))
            
        mins = [(0, -1)]
        for i, e in enumerate(a):
            if e < mins[-1][0]:
                mins.append((e, i))
        i, j = 0, 0
        
        ans = float('-inf')
        while i < len(mins) and j < len(maxs):
            v0, k0 = mins[i]
            v1, k1 = maxs[j]
            if k1-k0 >= k:
                ans = max(ans, v1 - v0)
                i += 1
            else:
                j += 1
        return ans
    
#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        ob = Solution()
        print(ob.maxSumWithK(a, n, k))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends