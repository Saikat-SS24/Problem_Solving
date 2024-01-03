""" Given a string S consisting of the characters 0, 1 and 2. Your task is to find the length of the smallest substring 
of string S that contains all the three characters 0, 1 and 2. If no such substring exists, then return -1.

Example 1:

Input:
S = 01212
Output:
3
Explanation:
The substring 012 is the smallest substring
that contains the characters 0, 1 and 2.

Example 2:

Input: 
S = 12121
Output:
-1
Explanation: 
As the character 0 is not present in the
string S, therefor no substring containing
all the three characters 0, 1 and 2
exists. Hence, the answer is -1 in this case.
Your Task:
Complete the function smallestSubstring() which takes the string S as input, and returns the length of the smallest 
substring of string S that contains all the three characters 0, 1 and 2.

Expected Time Complexity: O( length( S ) )
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ length( S ) ≤ 105
All the characters of String S lies in the set {'0', '1', '2'} """


#User function Template for python3

class Solution:
    def smallestSubstring(self, S):
        # Code here
        if '0' not in S or '1' not in S or '2' not in S:
            return -1
            
        res = []
        c = 10**5+1
        for i in S:
            if res == []:
                res.append(i)
            elif res[0] != i:
                res.append(i)
            elif res[0] == i:
                res.pop(0)
                res.append(i)
                j = 1
                while(len(res)>1 and j):
                    if(res[0] == res[1]):
                        res.pop(0)
                    else:
                        j = 0
            if '0' in res and '1' in res and '2' in res:
                c = min(c,len(res))
                res = []
        return c

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S = input()
		ob = Solution()
		ans = ob.smallestSubstring(S)
		
		print(ans)


# } Driver Code Ends