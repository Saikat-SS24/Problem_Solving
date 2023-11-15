""" Given a pair of strings of equal lengths, Geek wants to find the better string. The better string is the string 
having more number of distinct subsequences. If both the strings have equal count of distinct subsequence then return 
str1.

Example 1:

Input:
str1 = "gfg", str2 = "ggg"
Output: "gfg"
Explanation: "gfg" have 7 distinct subsequences whereas "ggg" have 4 distinct subsequences.

Example 2:

Input: str1 = "a", str2 = "b"
Output: "a"
Explanation: Both the strings have only 1 distinct subsequence. 
Your Task:
You don't need to read input or print anything. Your task is to complete the function betterString() which takes str1 
and str2 as input parameters and returns the better string.

Expected Time Complexity: O( max( str1.length, str2.length ) )

Expected Auxiliary Space: O( max( str1.length, str2.length ) )

Constraints:
1 <= str1.lenght , str2.length <= 30 """


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def distinct_subsequences(self, s):
        n = len(s)
        mod = 10**9 + 7
        dp = [0] * (n + 1)
        dp[0] = 1
        last_occurrence = {}
        for i in range(1, n + 1):
            dp[i] = (2 * dp[i - 1]) % mod
            if s[i - 1] in last_occurrence:
                dp[i] = (dp[i] - dp[last_occurrence[s[i - 1]] - 1] + mod) % mod
            last_occurrence[s[i - 1]] = i

        return dp[n]
        
    def betterString(self, str1, str2):
        # Code here
        return str1 if self.distinct_subsequences(str1)>=self.distinct_subsequences(str2) else str2
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        str1 = input()
        str2 = input()
        ob = Solution()
        res = ob.betterString(str1, str2)
        print(res)
# } Driver Code Ends