""" Given an array arr[] of positive integers. Find the number of pairs of integers whose difference equals a given 
number k.

Note: (a, b) and (b, a) are considered the same. Also, the same numbers at different indices are considered different.

Examples:

Input: arr[] = [1, 5, 3, 4, 2], k = 3
Output: 2
Explanation: There are 2 pairs with difference 3,the pairs are {1, 4} and {5, 2} 

Input: arr[] = [8, 12, 16, 4, 0, 20], k = 4
Output: 5
Explanation: There are 5 pairs with difference 4, the pairs are {0, 4}, {4, 8}, {8, 12}, {12, 16} and {16, 20}.

Constraints:
1 <= arr.size() <= 106
1 <= k <= 106
1 <= arri <= 106 """

#User function Template for python3
from collections import Counter

class Solution:
    def countPairsWithDiffK(self,arr, k):
        # code here
        n = len(arr)  
        freq = {}
        cnt = 0
    
        for i in range(n):
          
            # Check if the complement (arr[i] + k)
            # exists in the map. If yes, increment count
            if (arr[i] + k) in freq: 
                cnt += freq[arr[i] + k] 
          
            # Check if the complement (arr[i] - k)
            # exists in the map. If yes, increment count
            if (arr[i] - k) in freq: 
                cnt += freq[arr[i] - k] 
          
            # Increment the frequency of arr[i]
            freq[arr[i]] = freq.get(arr[i], 0) + 1 
        return cnt

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.countPairsWithDiffK(arr, k)
        print(ans)
        print("~")
        tc -= 1

# } Driver Code Ends