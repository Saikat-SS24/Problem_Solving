""" Given two integers L, R, and digit X. Find the number of occurrences of X in all the numbers in the range (L, R) 
excluding L and R.

Example 1:

Input:
L=10, R=19, X=1
Output:
9
Explanation:
There are 9 1s (11, 12, 13, 14, 15, 16, 17, 18) in the numbers in the range (10,19).

Example 2:

Input:
L=18, R=81, X=9
Output:
7
Explanation:
There are 7 occurrences of the digit 9 in the numbers in the range (18,81).
Your Task:
You don't need to read input or print anything. Your task is to complete the function countX() which takes three 
integers L, R, and X as input parameters and returns the number of occurrences of X in the numbers in the range(L, R).

Expected Time Complexity:O(RLogR)
Expected Auxillary Space:O(1)

Constraints:
1 <= L< R <= 105
0 <= X <= 9  """


#User function Template for python3

class Solution:    
    def countX(self,L,R,X):
        #code here
        rs_str = ''
        # converting the range(L+1, R) to string
        for i in range(L+1, R):
            rs_str += str(i)
         # returning the count of 'X
        return rs_str.count(str(X))



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        L,R,X=map(int,input().strip().split(" "))
        ob=Solution()
        ans=ob.countX(L,R,X)
        print(ans) 
# } Driver Code Ends