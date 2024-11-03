""" Given a string of S as input. Your task is to write a program to delete the minimum number of characters from the 
string so that the resultant string is a palindrome.
Note: The order of characters in the string should be maintained.

Example 1:

Input: 
S = "aebcbda"
Output: 
2
Explanation: 
Remove characters 'e' and 'd'.
Example 2:

Input: 
S = "geeksforgeeks"
Output: 
8
Explanation: 
One of the possible result string can be "eefee", so answer is 13 - 5 = 8.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function minimumNumberOfDeletions() 
which takes the string S as inputs and returns the minimum number of deletions required to convert S into a 
pallindrome.

Expected Time Complexity: O(|S|2)
Expected Auxiliary Space: O(|S|2)

Constraints:
1 ≤ |S| ≤ 103 """


#User function Template for python3

class Solution:
    def minimumNumberOfDeletions(self,S):
        # code here 
        n = len(S)
        # Create a 2D array to store the minimum deletions required for subproblems
        dp = [[0] * n for _ in range(n)]
        
        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                if (S[i] == S[j]):
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1
    
        # The minimum number of deletions to make a palindrome is stored in dp[0][n-1]
        return dp[0][n-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=input()

        ob = Solution()
        print(ob.minimumNumberOfDeletions(S))
# } Driver Code Ends