""" The problem is to count all the possible paths from top left to bottom right of an MxN matrix with the constraints
that from each cell you can either move to right or down.

Return answer modulo 109+7.

Example 1:

Input:
M = 3 and N = 3
Output: 6
Explanation:
Let the given input 3*3 matrix is filled 
as such:
A B C
D E F
G H I
The possible paths which exists to reach 
'I' from 'A' following above conditions 
are as follows:ABCFI, ABEHI, ADGHI, ADEFI, 
ADEHI, ABEFI
Example 2:

Input:
M = 1 and N = 4
Output: 1
Explanation:
There is only one direction to go in,
and thus, there is only one path possible.
Your Task
You don't need to read input or print anything. Your task is to complete the function numberOfPaths() which takes the 
integer M and integer N as input parameters and returns an integer, the number of paths.

Expected Time Complexity: O(M)
Expected Space Complexity: O(1)

Constraints:
1 ≤ N ≤ 108
1 ≤ M ≤ 105 """


#User function Template for python3

class Solution:
    def numberOfPaths (self, M, N):
        # code here
        path = 1
        Mod = 10**9 + 7
        for i in range(M - 1):
            path = (path*(i+N)) % Mod 
            temp = pow(i+1, Mod-2, Mod)
            path = (path*temp) % Mod
        return path



#{ 
 # Driver Code Starts
#Initial Template for Python 3

        

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        M, N = map(int, input().split())
        ans = ob.numberOfPaths(M, N)
        print(ans)



# } Driver Code Ends