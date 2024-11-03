""" You are given an integer N, reverse the digits of given number N, ensuring that the reversed number has no leading 
zeroes. Return the resulting reversed number.

Example 1:

Input: 200
Output: 2
Explanation: By reversing the digts of 
number, number will change into 2.

Example 2:

Input : 122
Output: 221
Explanation: By reversing the digits of 
number, number will change into 221.

Your Task:
You don't need to read or print anything. Your task is to complete the function reverse_digit() which takes N as input 
parameter and returns the reversed number.
 
Expected Time Complexity: O(Log(N))
Expected Space Complexity: O(1)
 

Constraints:
1 <= N <= 1015 """


#User function Template for python3

class Solution:
	def reverse_digit(self, n):
		# Code here
        rev_n = 0
        while n != 0:
            digit = n%10
            rev_n = rev_n*10 + digit
            n //= 10
            
        return rev_n

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.reverse_digit(n)
		print(ans)
# } Driver Code Ends