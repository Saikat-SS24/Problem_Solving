""" A function F is defined as follows F(n)= (1) +(2*3) + (4*5*6) ... upto n terms (look at the examples for better 
clarity). Given an integer n, determine the F(n).

Note: As the answer can be very large, return the answer modulo 109+7.

Example 1:

Input: n = 5
Output: 365527
Explanation: 
F(5) = 1 + 2*3 + 4*5*6 + 7*8*9*10 + 11*12*13*14*15 = 365527.

Example 2:

Input: n = 7
Output: 6006997207
Explanation: 
F(7) = 1 + 2*3 + 4*5*6 + 7*8*9*10 + 11*12*13*14*15 + 
16*17*18*19*20*21 + 22*23*24*25*26*27*28 = 6006997207.
6006997207 % 109+7 = 6997165
Your Task:
You do not need to read input or print anything. Your task is to complete the function sequence() which takes an 
integer n as an input parameter and returns the value of F(n).

Expected Time Complexity: O(n2)
Expected Space Complexity: O(1)

Constraints:
1 ≤ n ≤ 103 """


#User function Template for python3

class Solution:
    def sequence(self, n):
        # code here
        if n == 1:
            return 1
        mod = 1000000007
        sums = 0
        temp = 1
        for i in range(n):
            mul = 1
            for j in range(i+1):
                mul= (mul*temp) % mod
                temp +=1
            sums= (sums + mul)%mod
        return sums % mod

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        print(ob.sequence(N))
        
# } Driver Code Ends