""" Given an array A of size N. The value of an array is denoted by the bit-wise XOR of all elements it contains. Find 
the bit-wise XOR of the values of all subarrays of A.

Example 1:

Input: 
N = 3 
A = [1,2,3] 
Output: 
2
Explanation:
xor[1] = 1
xor[1, 2] = 3
xor[2, 3] = 1
xor[1, 2, 3] = 0
xor[2] = 2
xor[3] = 3
Result : 1 ^ 3 ^ 1 ^ 0 ^ 2 ^ 3 = 2

Example 2:

Input: 
N = 2
A = [1,2]
Output: 
0
Explanation:
xor[1] = 1
xor[1, 2] = 3
xor[2] = 2
Result : 1 ^ 3 ^ 2 = 0
Your Task:
You don't need to read input or print anything. Your task is to complete the function gameOfXor() which takes an 
integer N and array A[] as input parameters and returns the answer.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 <= N <= 105
0 <= A[i] <= 109 """


#User function Template for python3

class Solution:
    def gameOfXor(self, N , A):
        # code here 
        res = 0
        for i, e in enumerate(A):
            if (i+1)*(N-i)%2 == 0:
                res ^= 0
            else:
                res ^= e
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        A=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.gameOfXor(N,A))
# } Driver Code Ends