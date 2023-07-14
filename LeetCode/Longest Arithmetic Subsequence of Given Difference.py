class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        prevIndex = {}  # keeps track of closest index of integer
        dp = [0] * n
        ans = 0
        for i in range(n):
            prevNum = arr[i] - difference
            if prevNum in prevIndex:  # checks if prevNum was processed
                dp[i] = dp[prevIndex[prevNum]] + 1
            else:
                dp[i] = 1
            prevIndex[arr[i]] = i#the closest previous index of arr[i] is always i at this point
            ans = max(ans, dp[i])
        return ans