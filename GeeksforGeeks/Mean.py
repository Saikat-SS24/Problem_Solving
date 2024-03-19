""" Given the marks of N students in an Array A, calculate the mean.

Note: If result is a Decimal Value, find it's floor Value.

Example 1:

Input:
N = 4 
A = { 56 , 67 , 30 , 79 }
Output:
58
Explanation:
56+67+30+79 = 232;  232/4 = 58.
So, the Output is 58.

Example 2:

Input:
N = 4 
A = { 78 , 89 , 67 , 76 }
Output:
77
Explanation:
78+89+67+76  = 310;  310/4 = 77.5 = 77.
So, the Output is 77.
Your Task:
You don't need to read input or print anything. Your task is to complete the function mean() which takes 1 Integer N 
and an Array A as input and returns the answer.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 <= N <= 104
1 <= A[i] <= 104 """

#User function Template for python3

class Solution:
    def mean(self, N , A):
        # code here 
        sum = 0
        for i in range(N):
            sum = sum+A[i]
            
        res = int(sum/N)
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        A = list(map(int,input().split()))
        
        ob = Solution()
        print(ob.mean(N,A))

# } Driver Code Ends