""" Given a string str without spaces, the task is to remove all duplicate characters from it, keeping only the first 
occurrence.

Note: The original order of characters must be kept the same. 

Examples :

Input: str = "zvvo"
Output: "zvo"
Explanation: Only keep the first occurrence

Input: str = "gfg"
Output: "gf"
Explanation: Only keep the first occurrence

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 <= |str| <= 105
str contains lowercase English alphabets  """

#User function Template for python3
class Solution:
	def removeDups(self, str):
		# code here
        res = []
        for i in str:
            if i not in res:
                res.append(i)
        return "".join(res)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.removeDups(s)

        print(answer)


# } Driver Code Ends