""" Given two binary strings s1 and s2 consisting of only 0s and 1s. Find the resultant string after adding the two 
Binary Strings.

Note: The input strings may contain leading zeros but the output string should not have any leading zeros.

Input: s1 = "1101", s2 = "111"
Output: 10100
Explanation:
 1101
+ 111
10100

Input: s1 = "00100", s2 = "010"
Output: 110
Explanation: 
  100
+  10
  110

Constraints:
1 ≤s1.size(), s2.size()≤ 106 """

#User function Template for python3
class Solution:
    def addBinary(self, s1, s2):
        # code here
        return bin(int(s1,2) + int(s2,2))[2:]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        a = input().strip()
        b = input().strip()
        ob = Solution()
        answer = ob.addBinary(a, b)

        print(answer)
        print("~")

# } Driver Code Ends