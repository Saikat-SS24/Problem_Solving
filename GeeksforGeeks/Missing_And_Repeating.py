""" Given an unsorted array arr of of positive integers. One number 'A' from set {1, 2,....,n} is missing and one 
number 'B' occurs twice in array. Find numbers A and B.

Examples

Input: arr[] = [2, 2]
Output: 2 1
Explanation: Repeating number is 2 and smallest positive missing number is 1.

Input: arr[] = [1, 3, 3] 
Output: 3 2
Explanation: Repeating number is 3 and smallest positive missing number is 2.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
2 ≤ n ≤ 105
1 ≤ arr[i] ≤ n """

#User function Template for python3

class Solution:
    def findTwoElement( self,arr): 
        # code here
        n = len(arr)
        sum_of_n = n * (n + 1) // 2
        sum_of_n_squared = (n * (n + 1) * (2 * n + 1)) // 6
        
        sum_arr = sum(arr)
        sum_arr_squared = sum(x * x for x in arr)
        
        # Let missing = x, repeating = y
        # sum_arr = total_sum - x + y
        # sum_arr_squared = sum_of_n_squared - x^2 + y^2
        
        diff = sum_arr - sum_of_n  # This is y - x
        sum_diff = (sum_arr_squared - sum_of_n_squared) // diff  # This is y + x
        
        y = (diff + sum_diff) // 2
        x = sum_diff - y
        
        return (y, x) 

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findTwoElement(arr)
        print(str(ans[0]) + " " + str(ans[1]))
        tc = tc - 1

# } Driver Code Ends