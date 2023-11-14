""" You are given two strings of equal lengths, s1 and s2. The task is to check if s2 is a rotated version of the 
string s1.

Note: The characters in the strings are in lowercase.

Example 1:

Input:
geeksforgeeks
forgeeksgeeks
Output: 
1
Explanation: s1 is geeksforgeeks, s2 is
forgeeksgeeks. Clearly, s2 is a rotated
version of s1 as s2 can be obtained by
left-rotating s1 by 5 units.

Example 2:

Input:
mightandmagic
andmagicmigth
Output: 
0
Explanation: Here with any amount of
rotation s2 can't be obtained by s1.
Your Task:
You don't have to read or print anything. The task is to complete the function areRotations() which takes two strings,
s1 and s2 as inputs and checks if the two strings are rotations of each other. The function returns true if s1 can be 
obtained by rotating s2, else it returns false.

Expected Time Complexity: O( |s1| ).
Expected Space Complexity: O( |s1| ).

Constraints:
1 <= |s1|, |s2| <= 105 """


#User function Template for python3

class Solution:
    
    #Function to check if two strings are rotations of each other or not.
    def areRotations(self,s1,s2):
        #code here
        m = len(s1)
        n = len(s2)
        temp = ''
        # check if length is not same 
        if m != n:
            return False
        # Create a temp string with value s1.s1
        temp = s1+s1
        # Now check if s2 is a substring of temp
        # string.count returns the number of occurrences of
        # the second string in temp
        if (temp.count(s2) > 0):
            return True
        else:
            return False
        


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
        s1=str(input())
        s2=str(input())
        if(Solution().areRotations(s1,s2)):
            print(1)
        else:
            print(0)
    
        
# } Driver Code Ends