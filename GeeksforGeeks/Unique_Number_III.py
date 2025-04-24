""" Given an array of integers arr[] where, every element appears thrice except for one which occurs once.
Find that element which occurs once.

Examples:

Input: arr[] = [1, 10, 1, 1]
Output: 10
Explanation: 10 occurs once in the array while the other element 1 occurs thrice.

Input: arr[] = [3, 2, 1, 34, 34, 1, 2, 34, 2, 1]
Output: 3
Explanation: All elements except 3 occurs thrice in the array.

Constraints:
1 ≤ arr.size() ≤ 105
arr.size() % 3 = 1
-109 ≤ arr[i] ≤ 109 """

#User function Template for python3

class Solution:
    def getSingle(self, arr):
        # code here 
        unique_ele = set()
        total_sum = 0
        
        for i in arr:
            total_sum += i
            unique_ele.add(i)
            
        unique_sum = sum(unique_ele)
        res = (3*unique_sum - total_sum) // 2
        
        return res

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSingle(arr)
        print(ans)
        print("~")
# } Driver Code Ends