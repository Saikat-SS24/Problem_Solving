""" Given a positive integer n. You have to find nth natural number after removing all the numbers containing the 
digit 9.

Examples :

Input: n = 8
Output: 8
Explanation: After removing natural numbers which contains digit 9, first 8 numbers are 1,2,3,4,5,6,7,8 and 8th 
number is 8.

Input: n = 9
Output: 10
Explanation: After removing natural numbers which contains digit 9, first 9 numbers are 1,2,3,4,5,6,7,8,10 and 9th 
number is 10.

Expected Time Complexity: O(logn)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ n ≤ 109 """

#User function Template for python3

class Solution:
    def findNth(self,n):
        #code here
        result = 0
        p = 1
        # Iterate while n is
        # greater than 0
        while (n > 0):
          
            # Update result
            result += (p * (n % 9))
    
            # Divide n by 9
            n = n // 9
    
            # Multiply p by 10
            p = p * 10
        # Return result
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for i in range(0, t):
    n = int(input())
    obj = Solution()
    s = obj.findNth(n)
    print(s)

# } Driver Code Ends