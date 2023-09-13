""" Given two numbers 'N' and 'S' , find the largest number that can be formed with 'N' digits and 
whose sum of digits should be equals to 'S'. Return -1 if it is not possible.

Example 1:

Input: N = 2, S = 9
Output: 90
Explaination: It is the biggest number 
with sum of digits equals to 9.
Example 2:

Input: N = 3, S = 20
Output: 992
Explaination: It is the biggest number 
with sum of digits equals to 20.
Your Task:
You do not need to read input or print anything. Your task is to complete the function findLargest() which takes N and S as input parameters and returns the largest possible number. Return -1 if no such number is possible.

Expected Time Complexity: O(N)
Exepcted Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 104
0 ≤ S ≤ 105 """

#User function Template for python3

class Solution:
    def findLargest(self, N, S):
        # code here
        if S == 0 and N == 1: 
            return 0
        if S == 0 or 9 * N < S:
            return -1
        li = [0 for _ in range(N)]
        i = 0
        while S != 0:
            while S != 0 and li[i] != 9:
                li[i] += 1
                S -= 1
            i += 1
        return int(''.join(map(str,li)))

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, S = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.findLargest(N, S))
# } Driver Code Ends