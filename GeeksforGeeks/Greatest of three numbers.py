""" Given 3 numbers A, B and C. Find the greatest number among them.

Example 1:

Input: A = 10, B = 3, C = 2
Output: 10
Explanation:
10 is the greatest among the three.

Example 2:

Input: A = -4, B = -3, C = -2
Output: -2
Explanation:
-2 is the greatest among the three.

Your Task:
You don't need to read input or print anything.Your task is to complete the function greatestOfThree() which takes 
three numbers A,B and C as input parameters and returns the greatest among them.

Expected Time Complexity:O(1)
Expected Auxillary Space:O(1)

Constraints:
-109<=A,B,C<=109  """
#User function Template for python3

class Solution:
    def greatestOfThree(self,A,B,C):
        #code here
        res = []
        res.append(A)
        res.append(B)
        res.append(C)
        
        return max(res)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        A,B,C=map(int,input().strip().split(' '))
        ob=Solution()
        print(ob.greatestOfThree(A,B,C))   
# } Driver Code Ends