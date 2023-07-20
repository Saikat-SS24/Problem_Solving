# Given a string S consisting of lowercase Latin Letters. Return the first non-repeating character in S. 
# If there is no non-repeating character, return '$'.

# Input:
# S = hello
# Output: h
# Explanation: In the given string, the
# first character which is non-repeating
# is h, as it appears first and there is
# no other 'h' in the string.

# Input:
# S = zxvczbtxyzvy
# Output: c
# Explanation: In the given string, 'c' is
# the character which is non-repeating. 

#User function Template for python3

class Solution:
    
    #Function to find the first non-repeating character in a string.
    def nonrepeatingCharacter(self,s):
        #code here
        index = -1
        fnc = ""

        if len(s) == 0 :
            return '$'

        for i in s:
	        if s.count(i) == 1:
		        fnc += i
		        break
	        else:
		        index += 1
        if index == len(s)-1 :
            return '$'
        else:
	        return fnc
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

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
        obj = Solution()
        ans=obj.nonrepeatingCharacter(s)
        if(ans!='$'):
            print(ans)
        else:
            print(-1)
            
# } Driver Code Ends