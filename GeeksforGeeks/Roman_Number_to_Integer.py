""" Given a string in roman no format (s)  your task is to convert it to an integer . Various symbols and their 
values are given below.
I 1
V 5
X 10
L 50
C 100
D 500
M 1000

Example 1:

Input:
s = V
Output: 5
Example 2:

Input:
s = III 
Output: 3
Your Task:
Complete the function romanToDecimal() which takes a string as input parameter and returns the equivalent decimal 
number. 

Expected Time Complexity: O(|S|), |S| = length of string S.
Expected Auxiliary Space: O(1)

Constraints:
1<=roman no range<=3999 """

#User function Template for python3

class Solution:
    def romanToDecimal(self, S): 
        # code here
        roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        n = len(S)
        ans = 0
        for i in range(n-1,-1,-1):
            if i == n-1 or roman[S[i]] >= roman[S[i+1]]:
                ans += roman[S[i]]
            else:
                ans -= roman[S[i]]
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        ob = Solution()
        S = input()
        print(ob.romanToDecimal(S))
# } Driver Code Ends