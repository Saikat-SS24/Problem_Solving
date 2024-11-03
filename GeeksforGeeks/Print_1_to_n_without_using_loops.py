""" You are given an integer N. Print numbers from 1 to N without the help of loops.

Example 1:

Input:
N = 5
Output:
1 2 3 4 5
Explanation:
We have to print numbers from 1 to 5.

Example 2:

Input:
N = 10
Output:
1 2 3 4 5 6 7 8 9 10
Explanation:
We have to print numbers from 1 to 10.
Your Task:  
You don't need to read input. Your task is to complete the function printTillN() which takes an integer N as an input 
parameter and print numbers from 1 to N space-separated integers without the help of loops.

Note: print newline character at the end.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

Constraints:
1 ≤ N ≤ 1000  """

#User function Template for python3

class Solution:
    def printTillN(self, N):
    	#code here 
    	res = []
    	while N>0:
    	    res.append(N)
    	    N = N-1
    	res.sort()
        for i in range(0,len(res)):
            print(res[i],end=" ")


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printTillN(N)
        print()
# } Driver Code Ends