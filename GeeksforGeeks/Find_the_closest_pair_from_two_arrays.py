""" Given two sorted arrays arr and brr and a number x, find the pair whose sum is closest to x and the pair has an 
element from each array. In the case of multiple closest pairs return any one of them.
Note: Can return the two numbers in any manner.

Example 1:

Input : N = 4, M = 4
arr[ ] = {1, 4, 5, 7}
brr[ ] = {10, 20, 30, 40} 
X = 32
Output : 1
Explanation:
The closest pair whose sum is closest
to 32 is {1, 30} = 31.
Example 2:

Input : N = 4, M = 4
arr[ ] = {1, 4, 5, 7}
brr[ ] = {10, 20, 30, 40}
X = 50 
Output :  3 
Explanation: 
The closest pair whose sum is closest
to 50 is {7, 40} = 47.
Your Task:
You only need to complete the function printClosest() that takes an array (arr), another array (brr), size of array 
arr (N), size of array brr (M), and return the array of two integers whose sum is closest to X. The driver code takes 
care of the printing of the closest difference.

Expected Time Complexity: O(max(N,M)).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ N, M ≤ 105
1 ≤ A[i], B[i] ≤ 107 """

#User function Template for python3

class Solution:
    def printClosest (self,arr, brr, n, m, x) : 
        #code here
        d = float("inf")
        i = 0
        j = m-1
        list = []
        a,b = -1,-1
        while i<n and j>=0:
            if abs(arr[i]+brr[j]-x)<d:
                d = abs(arr[i]+brr[j]-x)
                a = arr[i]
                b = brr[j]
                
            if arr[i]+brr[j] > x:
                j -= 1
                
            else:
                i += 1
                
        list.extend([a,b])
        return list         
                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().strip().split()))
    brr = list(map(int, input().strip().split()))
    x = int(input())
    ob = Solution()
    ans = ob.printClosest(arr, brr, n, m, x)
    print(abs(ans[0]+ans[1] - x))
# } Driver Code Ends