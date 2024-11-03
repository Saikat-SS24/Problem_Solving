""" Given  two integers N and M. The problem is to find the number closest to N and divisible by M. If there are more 
than one such number, then output the one having maximum absolute value.

Example 1:

Input:
N = 13 , M = 4
Output:
12
Explanation:
12 is the Closest Number to
13 which is divisible by 4.

Example 2:

Input:
N = -15 , M = 6
Output:
-18
Explanation:
-12 and -18 are both similarly close to
-15 and divisible by 6. but -18 has
the maximum absolute value.
So, Output is -18
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function closestNumber() which takes an 
Integer n as input and returns the answer.

Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)

Constraints:
-105 <= N <= 105  """

#User function Template for python3

class Solution:
    def closestNumber(self, N , M):
        # code here 
        # Find the quotient
        q = int(N/M)
        # 1st possible closest number
        n1 = M*q
        # 2nd possible closest number
        if((N*M) > 0) :
            n2 = (M*(q + 1)) 
        else :
            n2 = (M*(q - 1))
        # if true, then n1 is the required closest number
        if (abs(N-n1) < abs(N-n2)) :
            return n1
         
        # else n2 is the required closest number 
        return n2


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,M=map(int,input().split())
        
        ob = Solution()
        print(ob.closestNumber(N,M))

# } Driver Code Ends