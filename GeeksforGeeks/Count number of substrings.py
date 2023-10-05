""" Given a string of lowercase alphabets, count all possible substrings (not necessarily distinct) that have exactly 
k distinct characters. 

Example 1:

Input:
S = "aba", K = 2
Output:
3
Explanation:
The substrings are: "ab", "ba" and "aba".
Example 2:

Input: 
S = "abaaca", K = 1
Output:
7
Explanation:
The substrings are: "a", "b", "a", "aa", "a", "c", "a". 
Your Task:
You don't need to read input or print anything. Your task is to complete the function substrCount() which takes the 
string S and an integer K as inputs and returns the number of substrings having exactly K distinct characters.

Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ |S| ≤ 106
1 ≤ K ≤ 26 """

#User function Template for python3


def solve(s,k):
        count = 0
        ans = ''
        d = dict()
        start = 0
        for i in range(len(s)):
            ans+=s[i]
            if s[i] in d:
                d[s[i]]+=1
            else:
                d[s[i]] = 1
            while len(d)>k:
                d[s[start]]-=1
                if d[s[start]]==0:
                    del d[s[start]]
                start+=1
                ans = ans[1:]
            count+=(i-start+1)
        return count
class Solution:
    def substrCount (self,s, k):
        # your code here
        return solve(s, k)-solve(s, k-1)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    k = int (input ())
    ob = Solution()
    print (ob.substrCount (s, k))
# } Driver Code Ends