""" Given a string consisting of lower case English alphabets, the task is to find the number of distinct 
subsequences of the string
Note: Answer can be very large, so, ouput will be answer modulo 109+7.

Example 1:

Input: 
s = "gfg"
Output: 
7
Explanation: 
The seven distinct subsequences are "", "g", "f", "gf", "fg", "gg" and "gfg" .
Example 2:

Input: 
s = "ggg"
Output: 
4
Explanation: 
The four distinct subsequences are "", "g", "gg", "ggg".
Your task:
You do not need to read any input or print anything. The task is to complete the function distinctSubsequences(), 
which takes a string as input and returns an integer.

Expected Time Complexity: O(|str|)
Expected Auxiliary Space: O(|str|)

Constraints:
1 ≤ |s| ≤ 105
s contains lower case English alphabets """

#User function Template for python3

class Solution:
	def distinctSubsequences(self, S):
		# code here
		dp = [0]*(len(S)+1)
        dp[0] = 1
        
        reg = dict()
        for i in range(1,len(dp)):
            dp[i] = 2*dp[i-1] % (10**9 + 7)
            cur = S[i-1]
            if cur in reg.keys():
                # get last time seen this char
                last_time_seen_cur = reg[cur]
                dp[i] = (dp[i] - dp[last_time_seen_cur-1]) % (10**9 + 7)
            reg[cur] = i
        return dp[-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()

		ob = Solution()
		answer = ob.distinctSubsequences(s)
		print(answer)

# } Driver Code Ends