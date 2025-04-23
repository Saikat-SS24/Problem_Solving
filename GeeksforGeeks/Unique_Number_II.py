""" Given an array arr[] containing 2*n + 2 positive numbers, out of which 2*n numbers exist in pairs whereas the 
other two number occur exactly once and are distinct. Find the other two numbers. Return the answer in increasing 
order.

Examples:

Input: arr[] = [1, 2, 3, 2, 1, 4]
Output: [3, 4] 
Explanation: 3 and 4 occur exactly once.

Input: arr[] = [2, 1, 3, 2]
Output: [1, 3]
Explanation: 1 and 3 occur exactly once.

Input: arr[] = [2, 1, 3, 3]
Output: [1, 2]
Explanation: 1 and 2 occur exactly once.

Constraints:
2 ≤ arr.size() ≤ 106 
1 ≤ arr[i] ≤ 5 * 106
arr.size() is even """

#User function Template for python3

class Solution:
    def singleNum(self, arr):
        # Code here
        n = len(arr)
        arr.sort()
        res = []
        i = 0
        while i < n:
            if i+1 < n and arr[i+1] == arr[i]:
                i += 2
            else:
                res.append(arr[i])
                i += 1
                
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))

        ob = Solution()
        ans = ob.singleNum(arr)

        print(" ".join(map(str, ans)))
        tc -= 1
        print("~")
# } Driver Code Ends