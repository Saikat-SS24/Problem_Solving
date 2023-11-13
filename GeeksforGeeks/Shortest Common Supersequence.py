""" Given two strings X and Y of lengths m and n respectively, find the length of the smallest string which has both, 
X and Y as its sub-sequences.
Note: X and Y can have both uppercase and lowercase letters.

Example 1

Input:
X = abcd, Y = xycd
Output: 6
Explanation: Shortest Common Supersequence
would be abxycd which is of length 6 and
has both the strings as its subsequences.

Example 2

Input:
X = efgh, Y = jghi
Output: 6
Explanation: Shortest Common Supersequence
would be ejfghi which is of length 6 and
has both the strings as its subsequences.
Your Task:
You don't have to take any input or print anything. Your task is to complete shortestCommonSupersequence() function 
that takes X, Y, m, and n as arguments and returns the length of the required string.

Expected Time Complexity: O(Length(X) * Length(Y)).
Expected Auxiliary Space: O(Length(X) * Length(Y)).

Constraints:
1<= |X|, |Y| <= 100 """

#User function Template for python3

class Solution:
    
    #Function to find length of shortest common supersequence of two strings.
    def shortestCommonSupersequence(self, X, Y, m, n):
        #code here
        dp=[[0]*(m+1) for _ in range(2)]
        for y in range(1,n+1):
            for x in range(1,m+1):
                if X[x-1]==Y[y-1]:
                    dp[y%2][x]=dp[(y-1)%2][x-1]+1
                else:
                    dp[y%2][x]=max(dp[(y-1)%2][x],dp[y%2][x-1])
        return m+n-dp[n%2][-1] 

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        X,Y=input().split()
        
        print(Solution().shortestCommonSupersequence(X,Y,len(X),len(Y)))
      
# } Driver Code Ends