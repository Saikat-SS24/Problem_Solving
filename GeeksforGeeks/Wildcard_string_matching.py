""" Given two strings wild and pattern. Determine if the given two strings can be matched given that, wild string may 
contain * and ? but string pattern will not. * and ? can be converted to another character according to the following 
rules:

* --> This character in string wild can be replaced by any sequence of characters, it can also be replaced by an empty 
string.
? --> This character in string wild can be replaced by any one character.
Example 1:

Input: 
wild = ge*ks
pattern = geeks
Output: Yes
Explanation: Replace the '*' in wild string 
with 'e' to obtain pattern "geeks".

Example 2:

Input: 
wild = ge?ks*
pattern = geeksforgeeks
Output: Yes
Explanation: Replace '?' and '*' in wild string with
'e' and 'forgeeks' respectively to obtain pattern 
"geeksforgeeks"
Your Task:
You don't need to read input or print anything. Your task is to complete the function match() which takes the string 
wild and pattern as input parameters and returns true if the string wild can be made equal to the string pattern, 
otherwise, returns false.

Expected Time Complexity: O(length of wild string * length of pattern string)
Expected Auxiliary Space: O(length of wild string * length of pattern string)

Constraints:
1 <= length of the two string <= 10^3  """


#User function Template for python3
import re

class Solution:
    def match(self, wild, pattern):
        # code here
        regex = "^" + wild.replace("?", "\w").replace("*", "\w*") + "$"
        return re.search(regex, pattern) is not None

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        wild = input()
        pattern = input()
        
        ob = Solution()
        if(ob.match(wild, pattern)):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends