## Isomorphic Strings

Given two strings s1 and s2 consisting of only lowercase English letters and of equal length, check if these two strings are isomorphic to each other.
If the characters in s1 can be changed to get s2, then two strings, s1 and s2 are isomorphic. A character must be completely swapped out for another character while maintaining the order of the characters. A character may map to itself, but no two characters may map to the same character.

Examples:

Input: s1 = "aab", s2 = "xxy"
Output: true
Explanation: Each character in s1 can be consistently mapped to a unique character in s2 (a → x, b → y).
Input: s1 = "aab", s2 = "xyz"
Output: false
Explanation: Same character 'a' in s1 maps to two different characters 'x' and 'y' in s2.
Input: s1 = "abc", s2 = "xxz"
Output: false
Explanation: Two different characters 'a' and 'b' in s1 maps with same character 'x' in s2. 
Constraints:
1 ≤ s1.size() = s2.size() ≤ 105 


```bash
#User function Template for python3
MAX_CHARS = 256

class Solution:
    
    #Function to check if two strings are isomorphic.
    def areIsomorphic(self,str1,str2):
        # code here
        m = len(str1)
        n = len(str2)
     
        # Length of both strings must be same for one to one
        # correspondence
        if m != n:
            return False
     
        # To mark visited characters in str2
        marked = [False] * MAX_CHARS
     
        # To store mapping of every character from str1 to
        # that of str2. Initialize all entries of map as -1
        map = [-1] * MAX_CHARS
     
        # Process all characters one by one
        for i in range(n):
     
            # if current character of str1 is seen first
            # time in it.
            if map[ord(str1[i])] == -1:
     
                # if current character of st2 is already
                # seen, one to one mapping not possible
                if marked[ord(str2[i])] == True:
                    return False
     
                # Mark current character of str2 as visited
                marked[ord(str2[i])] = True
     
                # Store mapping of current characters
                map[ord(str1[i])] = str2[i]
     
            # If this is not first appearance of current
            # character in str1, then check if previous
            # appearance mapped to same character of str2
            elif map[ord(str1[i])] != str2[i]:
                return False
     
        return True


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import defaultdict

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        ob = Solution()
        if(ob.areIsomorphic(s,p)):
            print(1)
        else:
            print(0)
            
# } Driver Code Ends
```