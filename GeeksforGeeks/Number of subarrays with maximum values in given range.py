""" Given an array of N elements and L and R, print the number of sub-arrays such that the value of the maximum array 
element in that subarray is at least L and at most R.

Example 1:

Input : 
Arr = {2, 0, 11, 3, 0}
L = 1 and R = 10
Output : 
4
Explanation:
The sub-arrays {2}, {2, 0}, {3} and {3, 0} have maximum in range 1-10.

Example 2:

Input : 
Arr = {3, 4, 1}
L = 2 and R = 4
Output : 
5
Explanation:
The sub-arrays {3}, {3, 4}, {3,4,1}, {4} and {4, 1} have maximum in range 2-4.
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the 
function countSubarrays() that takes an array arr, sizeOfArray (n), element L, integer R, and return the number of 
subarray with the maximum in range L-R. The driver code takes care of the printing.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ N ≤ 105
1 ≤ arr[i] ≤ 109
1 ≤ L ≤ R ≤ 109 """


#User function Template for python3

class Solution:
    def countSubarrays(self, a,n,L,R): 
        # Complete the function
        def nC2(n):
            return n * (n + 1) // 2
        
        def count_subarrays_at_most(arr, maxi):
            count, curr_len = 0, 0
            for a in arr:
                if a <= maxi:
                    curr_len += 1
                else:
                    count += nC2(curr_len)
                    curr_len = 0
            count += nC2(curr_len)
            return count
        
        return count_subarrays_at_most(a, R) - count_subarrays_at_most(a, L - 1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3



for _ in range(0,int(input())):
    n,l,r = map(int, input().strip().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    v = ob.countSubarrays(arr, n, l, r)
    print(v)
    
# } Driver Code Ends