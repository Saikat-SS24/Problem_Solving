""" Given a string str containing only lowercase letters, generate a string with the same letters, but in uppercase.

Example 1:

Input:
str = "geeks"
Output: GEEKS

Example 2:

Input:
str = "geeksforgeeks"
Output: GEEKSFORGEEKS
Your Task:
You don't need to read input or print anything. Your task is to complete the function to_upper() which takes the 
string str as an argument and returns the resultant string.

Expected Time Complexity: O(length of the string).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ length of the string ≤ 50 """

#User function Template for python3
class Solution:
    def to_upper(self, str):
        # code here
        res = str.upper()
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        str = input().strip()
        ob = Solution()
        print(ob.to_upper(str))

# } Driver Code Ends